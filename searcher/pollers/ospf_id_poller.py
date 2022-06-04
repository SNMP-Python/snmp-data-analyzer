from __future__ import absolute_import

from searcher.exceptions.ospf_id_not_available import OSPFIdNotAvailableException
from searcher.pollers.poller import Poll


OSPF_ID_OID = "OSPF-MIB::ospfRouterId"


class OSPFIdPoller(Poll):
    def poll(self) -> str:
        result = self.session.walk(OSPF_ID_OID)
        if len(result) != 1:
            raise OSPFIdNotAvailableException()
        return result[0].value
