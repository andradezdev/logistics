"""Compat shim. See ``goconnect.flight.exceptions``."""


try:
    from goconnect.flight.exceptions import *  # noqa: F401,F403
    from goconnect.flight.exceptions import (  # noqa: F401
    	APIAuthenticationError,
    	APIConnectionError,
    	APIRateLimitError,
    	AirlineNotFoundError,
    	AirportNotFoundError,
    	DataValidationError,
    	FlightNotFoundError,
    	FlightScheduleException,
    )
except ModuleNotFoundError:
    pass
