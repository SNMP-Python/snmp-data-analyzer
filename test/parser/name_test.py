from parser.exceptions.empty_sys_name import EmptySysNameException
from parser.router_parser_imp import RouterParserImp
from parser.value_objects.sys_name import SysName
from test.parser.mothers.router_primitive_mother import RouterPrimitiveMother

import pytest


def test_empty_sys_name_throws_exception():
    with pytest.raises(EmptySysNameException):
        RouterParserImp(RouterPrimitiveMother.get_one_router(sys_name="")).get_routers()


def test_correct_sys_name_saves_name():
    sys_name = (
        RouterParserImp(RouterPrimitiveMother.get_one_router(sys_name="pablo-pc"))
        .get_routers()[0]
        .sys_name
    )
    assert sys_name == SysName("pablo-pc")
