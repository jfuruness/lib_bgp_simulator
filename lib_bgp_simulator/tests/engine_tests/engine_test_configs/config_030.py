from ..graphs import Graph040
from ..utils import EngineTestConfig


from ....simulation_engine import BGPSimpleAS
from ....simulation_framework import ValidPrefix


class Custom30MultiValidPrefix(ValidPrefix):
    """A valid prefix engine input with multiple victims"""

    __slots__ = ()

    def _get_announcements(self):
        """Returns several valid prefix announcements"""
        vic_anns = super()._get_announcements()
        if vic_anns is None:
            return None

        for i in range(len(vic_anns)):
            if vic_anns[i].origin == 1:
                # longer path for AS 1
                vic_anns[i].as_path = (vic_anns[i].origin,
                                       vic_anns[i].origin,
                                       vic_anns[i].origin)
        return vic_anns


class Config030(EngineTestConfig):
    """Contains config options to run a test"""

    name = "030"
    desc = "Test seeded announcement should never be replaced"
    scenario = Custom30MultiValidPrefix(victim_asns={1, 4, 3, 5},
                                        num_victims=4,
                                        AdoptASCls=None,
                                        BaseASCls=BGPSimpleAS)
    graph = Graph040()
    non_default_as_cls_dict = dict()
    propagation_rounds = 1
