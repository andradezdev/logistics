"""Compat shim. See ``goconnect.land.providers.base``."""


try:
    from goconnect.land.providers.base import *  # noqa: F401,F403
    from goconnect.land.providers.base import (  # noqa: F401
    	CanSnapshot,
    	Event,
    	Position,
    	TelematicsProvider,
    	Temperature,
    )
except ModuleNotFoundError:
    pass
