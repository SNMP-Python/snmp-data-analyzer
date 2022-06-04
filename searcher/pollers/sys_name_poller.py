from __future__ import absolute_import

from searcher.pollers.poller import Poll


SYS_NAME_OID = "RFC1213-MIB::sysName.0"


class SysNamePoller(Poll):
    def poll(self) -> str:
        return self.session.get(SYS_NAME_OID).value
