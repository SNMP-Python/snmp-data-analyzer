from __future__ import absolute_import

from arg_parser.arg_parser import ArgParser, ParsedArgs


def test_default_args():
    parsed_args = ArgParser.get_args([])
    assert parsed_args == _get_expected_default_args()


def _get_expected_default_args():
    return ParsedArgs(ip_address=None, output_file=None, add_routes=False)


def test_ip_address_arg():
    parsed_args = ArgParser.get_args(["-i", "10.0.0.2"])
    assert parsed_args == _get_expected_ip_address_arg()


def _get_expected_ip_address_arg():
    return ParsedArgs(ip_address="10.0.0.2", output_file=None, add_routes=False)


def test_output_file_arg():
    parsed_args = ArgParser.get_args(["-o", "test.txt"])
    assert parsed_args == _get_expected_output_file_arg()


def _get_expected_output_file_arg():
    return ParsedArgs(ip_address=None, output_file="test.txt", add_routes=False)


def test_add_routes_arg():
    parsed_args = ArgParser.get_args(["-a"])
    assert parsed_args == _get_expected_add_routes_arg()


def _get_expected_add_routes_arg():
    return ParsedArgs(ip_address=None, output_file=None, add_routes=True)


def test_all_args():
    parsed_args = ArgParser.get_args(["-i", "10.0.0.2", "-o", "test.txt", "-a"])
    assert parsed_args == _get_expected_all_args()


def _get_expected_all_args():
    return ParsedArgs(ip_address="10.0.0.2", output_file="test.txt", add_routes=True)
