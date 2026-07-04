from src.parser import Parser

def test_encode_invalid_command():
    parser = Parser()
    assert parser.encode("INVALID_COMMAND") == []

def test_encode_ping():
    parser = Parser()
    assert parser.encode("PING") == [0xAA, 0x01, 0xAB]

