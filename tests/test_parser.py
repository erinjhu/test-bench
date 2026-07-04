import pytest
from src.parser import Parser

@pytest.mark.parametrize(
    "command, expected",
    [
        ("INVALID_COMMAND",  []),
        ("PING", [0xAA, 0x01, 0xAB]),
    ],
)
def test_encode_and_checksum(command, expected):
    parser = Parser()
    encoded_result = parser.encode(command)
    assert encoded_result == expected
    # [:-1] - everything but the last item
    # [-1] - last item
    if encoded_result:
        assert parser.checksum(encoded_result[:-1]) == encoded_result[-1]