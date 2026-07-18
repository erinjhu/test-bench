from src.hil import HILDriver
import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_hardware_ping():
    driver = HILDriver(port="/dev/ttyUSB0")
    driver.send_command("PING")
    response = driver.read_response()
    assert response["CMD"] == "PONG"

