from src.hil import HILDriver

def test_hardware_ping():
    driver = HILDriver(port="/dev/ttyUSB0")
    driver.send_command("PING")
    response = driver.read_response()
    assert response["CMD"] == "PONG"