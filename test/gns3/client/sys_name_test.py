from __future__ import absolute_import

import pytest

from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.snmp_client import SNMPClient

snmp_client = SNMPClient()


def test_non_reachable_host_throws_non_reachable_host_exception():
    with pytest.raises(NonReachableHostException):
        snmp_client.get_router_primitives('12.34.56.78')


def test_reachable_host_returns_name():
    # pylint: disable=E1111
    router_primitives = snmp_client.get_router_primitives('10.0.0.2')
    assert router_primitives.sys_name == 'SNMPv2-MIB::sysName.0 = STRING: R1'
