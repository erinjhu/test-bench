class Protocol:
    SOF = 0xAA

    VALUES = {
        "START_BYTE": 0xAA
    }

    PACKET_INDEX_NUM = {
        "START_BYTE": 0,
        "ID": 1,
        "DATA_LENGTH": 2,
        "PAYLOAD": 3,
        "CHECKSUM": -1
    }
    
    COMMAND_IDS = {
        "INVALID_GET": 0,
        # Control
        "PING":     0x01,
        "RESET":    0x02,
        # Telemetry/Read
        "GET_VOLT": 0x03,
        # Configuration/Write
        "INVALID_SET": 0,
        "SET_PWM":  0x04
    }