"""Compat shim. See ``goconnect.flight.aviation_edge.connector``."""


try:
    from goconnect.flight.aviation_edge.connector import *  # noqa: F401,F403
    from goconnect.flight.aviation_edge.connector import AviationEdgeConnector  # noqa: F401
except ModuleNotFoundError:
    pass
