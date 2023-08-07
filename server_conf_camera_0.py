import Pyro4

# Pyro4.config is a singleton, these changes to config will be
# used for all the device servers.  This needs to be done after
# importing microscope.device_server

# Serve a test camera.
from microscope.device_server import device
from microscope.simulators import SimulatedCamera

Pyro4.config.COMPRESSION = True
Pyro4.config.PICKLE_PROTOCOL_VERSION = 2


DEVICES = [
    device(SimulatedCamera, host="localhost", port=8000),
]
