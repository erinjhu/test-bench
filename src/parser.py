class Parser:

    """
    Translates human commands to binary packets.
    """
    COMMANDS = {
        # read commands
        "PING":0x01,
        "RESET":0x02,
        "GET_VOLT":0x03,
        # write commands
    }

    def encode(self, command_name, payload=None):
        """
        Converts command name into a list of bytes.

        Args:
            command_name (str): The command to send
            payload (): The data to send if it is a write command

        Returns:
            list: A list of bytes [START, ID, CHECKSUM] or empty list if invalid
        """
        start = 0xAA
        cmd_id = self.COMMANDS.get(command_name)
        if cmd_id is None:
            return[]
        checksum = (start + cmd_id) & 0xFF # 0xFF --> 1 byte
        return [start, cmd_id, checksum]
    
    def checksum(self, packet_bytes):
        return sum(packet_bytes[:-1]) & 0xFF