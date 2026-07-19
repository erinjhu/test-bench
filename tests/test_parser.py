import pytest
from src.parser import Parser
from src.constants import Protocol
# protocol: [START BYTE, ID BYTE, LENGTH BYTE, DATA BYTES, CHECKSUM BYTE]

# list (ordered, duplicates allowed): []
# set/dictionary (unordered, unique elements): {}

set_commands_data = [
    # (command name, id, payload length, payload, checksum)
    # case: payload length 1
    ("SET_PWM", Protocol.COMMAND_IDS["SET_PWM"], 1, 0x50, 0xFF),
]

# "command, expected_id, payload_input"
encode_commands_data = [
    # Control
    ("INVALID_COMMAND", Protocol.COMMAND_IDS["INVALID_GET"], None),
    ("PING", Protocol.COMMAND_IDS["PING"], None),
    # Telemetry/Read
    ("GET_VOLT", Protocol.COMMAND_IDS["GET_VOLT"], None),
    # Configuration/Write
    ("SET_PWM", Protocol.COMMAND_IDS["SET_PWM"], 0x50),
]


# ====================================================================
# Encode Commands
# ====================================================================

# expected: [start, cmd_id, data_length, payload, checksum]

@pytest.mark.parametrize("command, expected_id, payload_input", encode_commands_data)
def test_encode(command, expected_id, payload_input):
    parser = Parser()
    encoded_result = parser.encode(command, payload=payload_input)
    assert encoded_result[Protocol.PACKET_INDEX_NUM["START_BYTE"]] == Protocol.VALUES["START_BYTE"]        
    assert encoded_result[Protocol.PACKET_INDEX_NUM["ID"]] == expected_id
    if(payload_input is None): # for get commands
        assert encoded_result[Protocol.PACKET_INDEX_NUM["DATA_LENGTH"]] == 0
    else: # for set commands
        assert encoded_result[Protocol.PACKET_INDEX_NUM["DATA_LENGTH"]] == len(encoded_result[Protocol.PACKET_INDEX_NUM["PAYLOAD"]:Protocol.PACKET_INDEX_NUM["CHECKSUM"]])
    assert encoded_result[Protocol.PACKET_INDEX_NUM["CHECKSUM"]] == sum(encoded_result[:Protocol.PACKET_INDEX_NUM["CHECKSUM"]])
    # [:-1] - everything but the last item, [-1] - last item
    if encoded_result:
        assert parser.checksum(encoded_result[:Protocol.PACKET_INDEX_NUM["CHECKSUM"]]) == encoded_result[Protocol.PACKET_INDEX_NUM["CHECKSUM"]]

    # encoding for a range of inputs: e.g. 0-100 for pwm
   # case: longer payload - but don't really have any commands for that yet
   
# ====================================================================
# Valid Decode Commands
# ====================================================================


# test case
    # list of bytes
    # expected s

# decode function
    # reads the start, id, length
    # returns the response (remove the checksum)

decode_commands_data = [
    # response, expected_id
    [[0xAA, 0x01, 0x00, 0xAB], 0x01], # ping
    [[0xAA, 0x02, 0x00, 0xAC], 0x02] # reset
]

@pytest.mark.parametrize("response, expected_id", decode_commands_data)
def test_decode_no_payload(response, expected_id):
    parser = Parser()
    decoded_result = parser.decode(response)
    assert decoded_result["id"] == expected_id
    assert decoded_result["payload"] == []


# ====================================================================
# Invalid Decode Commands
# ====================================================================

    # case: invalid start byte
    # case: corrupted checksum
    # case: incorrect length

