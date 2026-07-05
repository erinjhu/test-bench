import pytest
from src.parser import Parser
from src.constants import Protocol

# protocol: [START, ID, LENGTH, DATA, CHECKSUM]

# list (ordered, duplicates allowed): []
# set/dictionary (unordered, unique elements): {}

get_commands_data = [
    ("INVALID_COMMAND", Protocol.COMMAND_IDS["INVALID_GET"]),
    ("PING", Protocol.COMMAND_IDS["PING"]),
    ("GET_VOLT", Protocol.COMMAND_IDS["GET_VOLT"]),
]

set_commands_data = [
    # (command name, id, payload length, payload, checksum)
    ("SET_PWM", Protocol.COMMAND_IDS["SET_PWM"], 1, 0x50, 0x54),
]

@pytest.mark.parametrize("command, expected_id", get_commands_data)
def test_encode_get_command(command, expected_id):
    parser = Parser()
    encoded_result = parser.encode(command)
    assert encoded_result == expected_id
    # [:-1] - everything but the last item
    # [-1] - last item
    if encoded_result:
        assert parser.checksum(encoded_result[:-1]) == encoded_result[-1]

@pytest.mark.parametrize("cmd_name, expected_id, expected_length, payload, expected_checksum", set_commands_data)
def test_encode_set_command(cmd_name, expected_id, expected_length, payload, expected_checksum):
    parser = Parser()
    packet = parser.encode(cmd_name, payload=payload)
    assert packet[1] == expected_id
    assert packet[2] == len(packet[3:-1]) # [include first index, exclude last index]
    assert packet[-1] == expected_checksum

# tests todo later
    # receive commands
    # encoding for a range of inputs: e.g. 0-100 for pwm