from ..graphs import Graph006
from ..utils import EngineTestConfig

from ....simulation_engine import BGPSimpleAS, ROVSimpleAS
from ....enums import ASNs
from ....simulation_framework import NonRoutedPrefixHijack


class Config011(EngineTestConfig):
    """Contains config options to run a test"""

    name = "011"
    desc = "NonRouted Prefix Hijack"
    scenario = NonRoutedPrefixHijack(attacker_asns={ASNs.ATTACKER.value},
                                     victim_asns={ASNs.VICTIM.value},
                                     AdoptASCls=ROVSimpleAS,
                                     BaseASCls=BGPSimpleAS)
    graph = Graph006()
    non_default_as_cls_dict = {
        2: ROVSimpleAS
    }
    propagation_rounds = 1
