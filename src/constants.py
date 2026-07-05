class Protocol:
    SOF = 0xAA
    
    COMMAND_IDS = {
        # Read
        "INVALID_GET": 0,
        "PING":     0x01,
        "GET_VOLT": 0x02,
        # Write
        "INVALID_SET": 0,
        "SET_PWM":  0x03
    }