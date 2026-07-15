import pytest
from src.parser import Parser
from src.constants import Protocol
from src.exceptions import InvalidCommandError, ChecksumMismatchError

# protocol: [START BYTE, ID BYTE, LENGTH BYTE, DATA BYTES, CHECKSUM BYTE]

# list (ordered, duplicates allowed): []
# set/dictionary (unordered, unique elements): {}

get_commands_data = [
    ("INVALID_COMMAND", Protocol.COMMAND_IDS["INVALID_GET"]),
    ("PING", Protocol.COMMAND_IDS["PING"]),
    ("GET_VOLT", Protocol.COMMAND_IDS["GET_VOLT"]),
]

set_commands_data = [
    # (command name, id, payload length, payload, checksum)
    # case: payload length 1
    ("SET_PWM", Protocol.COMMAND_IDS["SET_PWM"], 1, 0x50, 0xFF),
]

responses_data = [
    # bytes object 1
    # bytes object 2
]


# ====================================================================
# Valid Encode Commands
# ====================================================================

@pytest.mark.parametrize("command, expected_id", get_commands_data)
def test_encode_get_command(command, expected_id):
    parser = Parser()
    encoded_result = parser.encode(command, payload=None)
    assert encoded_result[Protocol.PACKET_INDEX_NUM["ID"]] == expected_id
    # [:-1] - everything but the last item
    # [-1] - last item
    if encoded_result:
        assert parser.checksum(encoded_result[:-1]) == encoded_result[-1]

@pytest.mark.parametrize("cmd_name, expected_id, expected_length, payload, expected_checksum", set_commands_data)
def test_encode_set_command(cmd_name, expected_id, expected_length, payload, expected_checksum):
    parser = Parser()
    packet = parser.encode(cmd_name, payload=payload)
    assert packet[Protocol.PACKET_INDEX_NUM["ID"]] == expected_id
    assert packet[Protocol.PACKET_INDEX_NUM["DATA_LENGTH"]] == len(packet[3:-1]) # [include first index, exclude last index]
    assert packet[Protocol.PACKET_INDEX_NUM["CHECKSUM"]] == expected_checksum

 # encoding for a range of inputs: e.g. 0-100 for pwm

   # case: longer payload


# ====================================================================
# Invalid Encode Commands
# ====================================================================


    # case: invalid start byte
    # case: corrupted checksum
    # case: incorrect length

   

# ====================================================================
# Valid Decode Commands
# ====================================================================

@pytest.mark.parametrize("responses", responses_data)
def test_decode(responses):

    # read the first section
        # assert that start byte is 0xAA
        # assert that id == expected id
        # assert that length == expected length

    # read the data
        # stm32 is little endian, system is big endian
    assert 1

# test case
    # list of bytes
    # expected s

# decode function
    # reads the start, id, length
    # returns the response (remove the checksum)

# ====================================================================
# Invalid Decode Commands
# ====================================================================

    # case: invalid start byte
    # case: corrupted checksum
    # case: incorrect length

