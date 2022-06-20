from itertools import chain

from yamlable import YamlAble, yaml_info, yaml_info_decorate

from ..enums import Relationships

_all_slots = dict()


# Because of the two issues below, we MUST use
# unsafe_hash and not frozen
# We can't use their backports
# Because we inherit announcements
# So the slots in an announcement != vars
# When python3.10 is supported by pypy3, we can
# use Frozen properly
# https://stackoverflow.com/q/55307017/8903959
# https://bugs.python.org/issue45520
@yaml_info(yaml_tag="Announcement")
class Announcement(YamlAble):
    """MRT Announcement"""

    # I ran tests for 50 trials for 20% adoption for ROV
    # On average, with slots and pypy, an average of 207 seconds
    # But without slots, more RAM, but 175 seconds
    # I ran a lot of these trials and this was very consistent
    # extremely low standard deviation. Maybe 1s difference across trials
    # My thought is twofold. One is that maybe object creation with slots
    # Is slightly slower, but less RAM with faster attr access
    # Maybe this has to do with deepcopy doing better without slots
    # Or maybe pypy is more optimized without slots since it's more common
    # No reason to figure out exactly why, but turning off slots for
    # Slightly more RAM but slightly faster trials makes sense to me since
    # We have very few prefixes per attack. If that ever changes
    # Maybe it makes sense to add this back
    # Additionally, without slots, I tried making it according to the RFC
    # I added dicts for simulation attrs, path attrs, transitive, non trans
    # But this was much slower, 228 seconds
    # NOTE: All of this was when we were deep copying announcements instead of
    # Creating new ones from scratch. After creating new ones from scratch,
    # Trials were more than twice as fast, completing between 90-95s without
    # slots
    # With slots, around 88-89s per trial. Not much of a difference, but also
    # less ram
    # And it's just faster. We'd have to do larger timing tests to find out
    # more
    # NOTE: also add prefix_id reasoning to design_decisions
    __slots__ = (
        "prefix",
        "timestamp",
        "as_path",
        "roa_valid_length",
        "roa_origin",
        "recv_relationship",
        "seed_asn",
        "withdraw",
        "traceback_end",
    )

    def __init__(
        self,
        *,
        prefix: str,
        as_path: tuple,
        timestamp: int,
        seed_asn: int,
        roa_valid_length: bool,
        roa_origin: int,
        recv_relationship: Relationships,
        withdraw: bool = False,
        traceback_end: bool = False,
        communities: tuple = (),
    ):
        self.prefix: str = prefix
        self.as_path: tuple = as_path
        self.timestamp: int = timestamp
        self.seed_asn: int = seed_asn
        self.roa_valid_length: bool = roa_valid_length
        self.roa_origin: int = roa_origin
        self.recv_relationship: Relationships = recv_relationship
        self.withdraw: bool = withdraw
        self.traceback_end: bool = traceback_end
        self.communities: tuple = communities

    def __init_subclass__(cls, *args, **kwargs):
        """This method essentially creates a list of all subclasses
        This is allows us to easily assign yaml tags
        """

        super().__init_subclass__(*args, **kwargs)
        yaml_info_decorate(cls, yaml_tag=cls.__name__)

    def __eq__(self, other):
        if isinstance(other, Announcement):
            return self._get_vars() == other._get_vars()
        else:
            return NotImplemented

    def prefix_path_attributes_eq(self, ann):
        """Checks prefix and as path equivalency"""

        if ann is None:
            return False
        elif isinstance(ann, Announcement):
            return (ann.prefix, ann.as_path) == (self.prefix, self.as_path)
        else:
            raise NotImplementedError

    def copy(self, **extra_kwargs):
        """Creates a new ann with proper sim attrs"""

        kwargs = self._get_vars()
        # Replace seed asn and traceback end every time by default
        kwargs["seed_asn"] = None
        kwargs["traceback_end"] = False
        kwargs.update(extra_kwargs)

        return self.__class__(**kwargs)

    @property
    def invalid_by_roa(self) -> bool:
        """Returns True if Ann is invalid by ROA

        False means ann is either valid or unknown
        """

        # Not covered by ROA, unknown
        if self.roa_origin is None:
            return False
        else:
            return self.origin != self.roa_origin or not self.roa_valid_length

    @property
    def valid_by_roa(self) -> bool:
        """Returns True if Ann is valid by ROA

        False means ann is either invalid or unknown
        """

        return self.origin == self.roa_origin and self.roa_valid_length

    @property
    def unknown_by_roa(self) -> bool:
        """Returns True if ann is not covered by roa"""

        return self.origin is None

    @property
    def covered_by_roa(self):
        """Returns if an announcement has a roa"""

        return not self.unknown_by_roa

    @property
    def roa_routed(self):
        return self.roa_origin != 0

    @property
    def origin(self) -> int:
        return self.as_path[-1]

    @property
    def all_slots(self):
        """Returns all slots including of parent classes"""

        global _all_slots
        cls_slots = _all_slots.get(self.__class__)

        # singleton for speed
        if not cls_slots:
            # https://stackoverflow.com/a/6720815/8903959
            cls_slots = chain.from_iterable(
                getattr(cls, "__slots__", []) for cls in self.__class__.__mro__
            )
            cls_slots = tuple(list(cls_slots))
            _all_slots[self.__class__] = cls_slots
        return cls_slots

    def __str__(self):
        return f"{self.prefix} {self.as_path} {self.recv_relationship}"

    def _get_vars(self):
        """Returns class as a dict

        (Can't use normal vars due to slots)"""

        return {x: getattr(self, x) for x in self.all_slots}

    ##############
    # Yaml funcs #
    ##############

    def __to_yaml_dict__(self):
        """This optional method is called when you call yaml.dump()"""

        return self._get_vars()

    @classmethod
    def __from_yaml_dict__(cls, dct, yaml_tag):
        """This optional method is called when you call yaml.load()"""

        return cls(**dct)
