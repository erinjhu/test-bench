"""Custom exceptions for STM32 serial communication protocol"""

class ProtocolError(Exception):
    """Base exception for protocol-related errors
    """
    pass

# =====================================================================
# Encoding Errors (Host -> STM32)
# =====================================================================

class InvalidCommandError(ProtocolError):
    """Raised when a command ID is invalid"""
    pass


class PayloadTooLargeError(ProtocolError):
    """Raised when the data payload exceeds the maximum allowed size (255 bytes)."""
    pass


# =====================================================================
# Decoding Errors (STM32 -> Host)
# =====================================================================

class InvalidStartByteError(ProtocolError):
    """Raised when the incoming packet does not begin with the expected START byte."""
    pass


class LengthMismatchError(ProtocolError):
    """Raised when the actual number of received bytes does not match the LENGTH byte."""
    pass


class ChecksumMismatchError(ProtocolError):
    """Raised when the calculated checksum does not match the received checksum byte."""
    pass
