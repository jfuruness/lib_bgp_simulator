from ..graphs import Graph040
from ..utils import EngineTestConfig

from ....simulation_engine import BGPSimpleAS
from ....simulation_framework import ValidPrefix


class Config028(EngineTestConfig):
    """Contains config options to run a test"""

    name = "028"
    desc = "Test of peer preference"
    scenario = ValidPrefix(victim_asns={2, 3},
                           num_victims=2,
                           AdoptASCls=None,
                           BaseASCls=BGPSimpleAS)
    graph = Graph040()
    non_default_as_cls_dict = dict()
    propagation_rounds = 1
