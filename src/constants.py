class Protocol:
    SOF = 0xAA

    

    PACKET_INDEX_NUM = {
        "ID": 1,
        "DATA_LENGTH": 2,
        "CHECKSUM": -1
    }
    
    COMMAND_IDS = {
        # Read
        "INVALID_GET": 0,
        "PING":     0x01,
        "RESET":    0x02,
        "GET_VOLT": 0x03,
        # Write
        "INVALID_SET": 0,
        "SET_PWM":  0x04
    }