import pytest
import sys # for python runtime environment system functions/variables
import serial

def test_python_version():
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 10

def test_serial_library_import():
    # verify pyserial is installed and accessible in the container
    try:
        # check if the module exists
        assert serial.__version__ is not None
    except ImportError:
        pytest.fail("pyserial is not installed in the Docker container")

def test_basic_logic():
    assert 1 + 1 == 2