"""Compat shim. See ``goconnect.land.providers.traccar``."""


try:
    from goconnect.land.providers.traccar import *  # noqa: F401,F403
    from goconnect.land.providers.traccar import TraccarProvider  # noqa: F401
except ModuleNotFoundError:
    pass
