from parser.interface_remover import InterfaceRemover
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType
from test.shared.interface_mothers import InterfaceMother
from test.shared.router_mothers import RouterMother


def test_router_without_down_or_loopback_is_the_same():
    interface = InterfaceMother.get_interface_with_status(status=InterfaceStatus.UP)
    router = RouterMother.get(interfaces=[interface])
    InterfaceRemover.remove_down_and_loopback([router])
    assert set(router.interfaces) == {interface}


def test_router_with_down_interface_removes_it():
    interface_1 = InterfaceMother.get_interface_with_status(status=InterfaceStatus.UP)
    interface_2 = InterfaceMother.get_interface_with_status(status=InterfaceStatus.DOWN)
    router = RouterMother.get(interfaces=[interface_1, interface_2])
    InterfaceRemover.remove_down_and_loopback([router])
    assert set(router.interfaces) == {interface_1}


def test_router_with_loopback_interface_removes_it():
    interface_1 = InterfaceMother.get_interface_with_type(type = InterfaceType.NORMAL)
    interface_2 = InterfaceMother.get_interface_with_type(type = InterfaceType.LOOPBACK)
    router = RouterMother.get(interfaces=[interface_1, interface_2])
    InterfaceRemover.remove_down_and_loopback([router])
    assert set(router.interfaces) == {interface_1}
