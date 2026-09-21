"""Compat shim. See ``goconnect.flight.base_flight_connector``."""


try:
    from goconnect.flight.base_flight_connector import *  # noqa: F401,F403
    from goconnect.flight.base_flight_connector import BaseFlightConnector  # noqa: F401
except ModuleNotFoundError:
    pass
