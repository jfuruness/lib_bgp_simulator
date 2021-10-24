from typing import List, Optional

from ..bgp_as import BGPAS

from ....announcements import Announcement as Ann
from ....enums import Relationships


def _propagate(self,
               propagate_to: Relationships,
               send_rels: List[Relationships]):
    """Propogates announcements to other ASes

    send_rels is the relationships that are acceptable to send
    """
    # _policy_propagate and _add_ann_to_q have been overriden
    # So that instead of propagating, announcements end up in the _send_q
    # Send q contains both announcements and withdrawals
    self._populate_send_q(propagate_to, send_rels)

    # Send announcements/withdrawals and add to ribs out
    self._send_anns(propagate_to)


def _policy_propagate(self,
                      neighbor: BGPAS,
                      ann: Ann,
                      *args,
                      **kwargs) -> bool:
    """Don't send what we've already sent"""

    ribs_out_ann: Optional[Ann] = self._ribs_out.get_ann(neighbor.asn,
                                                         ann.prefix)
    return ann.prefix_path_attributes_eq(ribs_out_ann)


def _process_outgoing_ann(self, neighbor: BGPAS, ann: Ann, *args):
    self._send_q.add_ann(neighbor.asn, ann)


def _send_anns(self, propagate_to: Relationships):
    """Sends announcements and populates ribs out"""

    neighbors: List[BGPAS] = getattr(self, propagate_to.name.lower())

    for (neighbor, prefix, ann) in self._send_q.info(neighbors):
        neighbor.receive_ann(ann)
        # Update Ribs out if it's not a withdraw
        if not ann.withdraw:
            self._ribs_out.add_ann(neighbor.asn, ann)
    for neighbor in getattr(self, propagate_to.name.lower()):
        self._send_q.reset_neighbor(neighbor.asn)