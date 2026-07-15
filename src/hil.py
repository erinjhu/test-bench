import serial
from src.parser import Parser

class HILDriver:
    def __init__(self, port):
        self.ser = serial.Serial(port, 115200)
        self.parser = Parser()

    def send_command(self, cmd, payload=None):
        packet = self.parser.encode(cmd, payload)
        self.ser.write(bytes(packet))