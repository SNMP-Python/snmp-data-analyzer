from parser.exceptions.empty_interface_name import EmptyInterfaceNameException
from parser.exceptions.empty_speed_value import SpeedValueException
from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from parser.exceptions.status_value_exception import StatusValueException
from parser.router_parser_imp import RouterParserImp
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType
from test.shared.interface_primitive_mothers import InterfacePrimitiveMother
from test.shared.router_primitive_mother import RouterPrimitiveMother

import pytest
from netaddr import IPNetwork


def test_speed_throws_exception_if_value_is_empty():
    interface = InterfacePrimitiveMother.get_list_of_one_element(speed="")
    with pytest.raises(SpeedValueException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_speed_not_a_double_throws_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(speed="2a")
    with pytest.raises(SpeedValueException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_speed_that_is_an_integer_does_not_throw_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(speed="2")
    speed = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .speed
    )
    assert speed == SpeedInterface("2")


def test_speed_that_is_a_negative_number_throws_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(speed="-232452345")
    with pytest.raises(SpeedValueException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_empty_interface_name_throws_empty_interface_name_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(name="")
    with pytest.raises(EmptyInterfaceNameException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_correct_interface_returns_name():
    interface = InterfacePrimitiveMother.get_list_of_one_element(name="eth0")
    interface_name = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .name
    )
    assert interface_name == InterfaceName("eth0")


def test_empty_interface_status_throws_status_value_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(status="")
    with pytest.raises(StatusValueException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_not_supported_status_throws_status_value_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(
        status=InterfacePrimitiveMother.INCORRECT_STATUS
    )
    with pytest.raises(StatusValueException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_up_value_gets_correct_status():
    interface = InterfacePrimitiveMother.get_list_of_one_element(
        status=InterfacePrimitiveMother.STATUS_UP
    )
    status = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .status
    )
    assert status == InterfaceStatus.UP


def test_down_value_gets_correct_status():
    interface = InterfacePrimitiveMother.get_list_of_one_element(
        status=InterfacePrimitiveMother.STATUS_DOWN
    )
    status = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .status
    )
    assert status == InterfaceStatus.DOWN


def test_empty_ip_does_throw_invalid_ip_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(ip="")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_not_valid_ip_does_throw_invalid_ip_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(ip="1.1.1.1.1.1")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_valid_ip_does_not_throw_invalid_ip_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(ip="1.1.1.1")
    RouterParserImp(
        RouterPrimitiveMother.get_one_router(interfaces=interface)
    ).get_routers()


def test_empty_mask_throw_invalid_mask_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(mask="")
    with pytest.raises(InvalidMaskException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_not_valid_mask_throws_invalid_ip_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(
        mask="255.255.255.255.255.255"
    )
    with pytest.raises(InvalidMaskException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_valid_mask_does_not_throw_invalid_ip_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(mask="255.255.255.0")
    RouterParserImp(
        RouterPrimitiveMother.get_one_router(interfaces=interface)
    ).get_routers()


def test_valid_mask_and_ip_returns_correct_network():
    interface = InterfacePrimitiveMother.get_list_of_one_element(
        ip="10.3.2.1", mask="255.255.255.0"
    )
    network = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .network
    )
    assert network == IPNetwork("10.3.2.0/24")


def test_invalid_interface_type_throws_exception():
    interface = InterfacePrimitiveMother.get_list_of_one_element(int_type="aa")
    with pytest.raises(ValueError):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(interfaces=interface)
        ).get_routers()


def test_valid_interface_type_loopback():
    interface = InterfacePrimitiveMother.get_list_of_one_element(int_type="24")
    type_int = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .type_interface
    )
    assert type_int == InterfaceType.LOOPBACK


def test_valid_interface_type_normal():
    interface = InterfacePrimitiveMother.get_list_of_one_element(int_type="6")
    type_int = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(interfaces=interface))
        .get_routers()[0]
        .interfaces[0]
        .type_interface
    )
    assert type_int == InterfaceType.NORMAL
