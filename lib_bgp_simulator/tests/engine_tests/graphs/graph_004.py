from lib_caida_collector import CustomerProviderLink as CPLink

from .graph_info import GraphInfo
from ....enums import ASNs


class Graph004(GraphInfo):
    r"""v2 example with ROV++V1 and ROV

              /1\
             / / \\attacker_asn
            /  2 \
           /  /    5
          4  3    \
           | /       victim_asn
          6
          / \
         7 8
        """

    def __init__(self):
        super(Graph004, self).__init__(
            customer_provider_links=set(
                [CPLink(provider_asn=1, customer_asn=4),
                 CPLink(provider_asn=1, customer_asn=2),
                 CPLink(provider_asn=1, customer_asn=5),
                 CPLink(provider_asn=1, customer_asn=ASNs.ATTACKER.value),
                 CPLink(provider_asn=4, customer_asn=6),
                 CPLink(provider_asn=6, customer_asn=7),
                 CPLink(provider_asn=6, customer_asn=8),
                 CPLink(provider_asn=2, customer_asn=3),
                 CPLink(provider_asn=3, customer_asn=6),
                 CPLink(provider_asn=5, customer_asn=ASNs.VICTIM.value)]))
