from __future__ import absolute_import

from typing import List

from searcher.pollers.poller import Poll


OSPF_BEIGHBORS_OID = "OSPF-MIB::ospfNbrIpAddr"


class OSPFNeighborsPoller(Poll):
    def poll(self) -> List[str]:
        return list(
            map(
                lambda neighbor: neighbor.value,
                self.session.walk(OSPF_BEIGHBORS_OID),
            )
        )
