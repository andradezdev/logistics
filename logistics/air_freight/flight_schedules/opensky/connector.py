"""Compat shim. See ``goconnect.flight.opensky.connector``."""


try:
    from goconnect.flight.opensky.connector import *  # noqa: F401,F403
    from goconnect.flight.opensky.connector import OpenSkyConnector  # noqa: F401
except ModuleNotFoundError:
    pass
