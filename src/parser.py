class Parser:
    """
    Translates human commands to binary packets.
    """
    COMMANDS = {
        "PING":0x01,
        "RESET":0x02,
        "GET_VOLT":0x02,
    }
    def encode(self, command_name):
        """
        Converts command name into a list of bytes.

        Args:
            command_name (str): The command to send

        Returns:
            list: A list of bytes [START, ID, CHECKSUM] or empty list if invalid
        """
        if command_name not in self.COMMANDS:
            return []
        if command_name == "PING":
            start = 0xAA
            cmd_id = 0x01
            checksum = (start + cmd_id) & 0xFF # 0xFF --> 1 byte
            return [start, cmd_id, checksum]
        return []