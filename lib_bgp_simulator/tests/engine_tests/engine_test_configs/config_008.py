from ..graphs import Graph003
from ..utils import EngineTestConfig

from ....simulation_engine import ROVAS
from ....simulation_engine import BGPAS
from ....enums import ASNs
from ....simulation_framework import SubprefixHijack


class Config008(EngineTestConfig):
    """Contains config options to run a test"""

    name = "008"
    desc = "Fig 2 (ROVSimpleAS)"
    scenario = SubprefixHijack(attacker_asns={ASNs.ATTACKER.value},
                               victim_asns={ASNs.VICTIM.value},
                               AdoptASCls=ROVAS,
                               BaseASCls=BGPAS,
                               )

    graph = Graph003()
    non_default_as_cls_dict = {3: ROVAS,
                               4: ROVAS}
    propagation_rounds = 1
