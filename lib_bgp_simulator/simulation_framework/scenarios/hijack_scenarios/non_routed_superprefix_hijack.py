from ..scenario import Scenario
from ....enums import Prefixes
from ....enums import Relationships
from ....enums import Timestamps


class NonRoutedSuperprefixHijack(Scenario):
    """Non routed superprefix hijack

    Attacker has a superprefix with an unknown ROA,
    hijacking a non routed prefix that has a non routed ROA
    """

    __slots__ = ()  # type: ignore

    def _get_announcements(self) -> tuple:
        """Returns a superprefix announcement for this engine input

        for subclasses of this EngineInput, you can set AnnCls equal to
        something other than Announcement
        """

        anns: list = list()
        for attacker_asn in self.attacker_asns:
            anns.append(self.AnnCls(prefix=Prefixes.SUPERPREFIX.value,
                                    as_path=(attacker_asn,),
                                    timestamp=Timestamps.ATTACKER.value,
                                    seed_asn=attacker_asn,
                                    roa_valid_length=None,
                                    roa_origin=None,
                                    recv_relationship=Relationships.ORIGIN))

        return tuple(anns)
