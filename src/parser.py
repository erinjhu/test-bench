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
        if payload is None:
            payload = []
            payload_length = 0
        else:   
            if isinstance(payload, int): # check if payload is a single int
                payload = [payload] # format as a list
                payload_length = 1
            elif not isinstance(payload, list):
                raise TypeError("payload must be an int or list of bytes")
            elif any(not isinstance(b, int) or b < 0 or b > 255 for b in payload):
                raise ValueError("payload must contain only byte values from 0 to 255")
            else:
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
    
    
    def decode(self, response):
        """
        Parses the bytes response received from the microcontroller 

        Args:
            response (dictionary): The response received

        Returns:
            dictionary: Values {"command_id": int, "payload": list[int]}
        """

        length = response[Protocol.PACKET_INDEX_NUM["DATA_LENGTH"]]
        payload_start = Protocol.PACKET_INDEX_NUM["PAYLOAD"]
         # if length is 0, the payload will be []
        payload = response[payload_start : payload_start + length]

        return {
            "id": response[Protocol.PACKET_INDEX_NUM["ID"]],
            "payload": payload
        }

