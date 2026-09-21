"""Compat shim. See ``goconnect.flight.aviationstack.connector``."""


try:
    from goconnect.flight.aviationstack.connector import *  # noqa: F401,F403
    from goconnect.flight.aviationstack.connector import AviationStackConnector  # noqa: F401
except ModuleNotFoundError:
    pass
