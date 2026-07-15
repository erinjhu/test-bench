from src.constants import Protocol

class Parser:

    """
    Translates human commands to binary packets.
    """

    def encode(self, command_name, payload=None):
        """
        Converts command name into a list of bytes.

        Args:
            command_name (str): The command to send
            payload (): The data to send if it is a write command

        Returns:
            list: A list of bytes [START, ID, CHECKSUM] or empty list if invalid
        """
        # check if payload is valid
        if payload is None:
            payload = []
        elif isinstance(payload, int): # check if payload is a single int
            payload = [payload] # format as a list
        elif not isinstance(payload, list):
            raise TypeError("payload must be an int or list of bytes")
        if any(not isinstance(b, int) or b < 0 or b > 255 for b in payload):
            raise ValueError("payload must contain only byte values from 0 to 255")
        payload_length = len(payload)

        start = Protocol.VALUES["START_BYTE"]
        if command_name not in Protocol.COMMAND_IDS:
            cmd_id = 0
        else:
            cmd_id = Protocol.COMMAND_IDS[command_name]
        packet = [start, cmd_id, payload_length]
        packet.extend(payload)
        checksum = self.checksum(packet)
        packet.append(checksum)
        return packet
    
    def checksum(self, bytes_to_sum):
        return sum(bytes_to_sum) & 0xFF
    
    """
    Parses the bytes response received from the microcontroller
    """
    
    def decode(self, response):
        return