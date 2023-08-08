import Pyro4

from microscope.device_server import device
from microscope.simulators import SimulatedLightSource

Pyro4.config.COMPRESSION = True
Pyro4.config.PICKLE_PROTOCOL_VERSION = 2


DEVICES = [
    device(SimulatedLightSource, host="light_0", port=9000),
]
