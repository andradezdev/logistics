"""Compat shim. See ``goconnect.flight.aggregator`` for the real module."""


try:
    from goconnect.flight.aggregator import *  # noqa: F401,F403
    from goconnect.flight.aggregator import (  # noqa: F401
    	FlightScheduleAggregator,
    	get_aggregator,
    )
except ModuleNotFoundError:
    pass
