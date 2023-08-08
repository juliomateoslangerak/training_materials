import Pyro4

from microscope.device_server import device
from microscope.simulators import SimulatedCamera

Pyro4.config.COMPRESSION = True
Pyro4.config.PICKLE_PROTOCOL_VERSION = 2


DEVICES = [
    device(SimulatedCamera, host="camera_0", port=8000),
]
