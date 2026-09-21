"""Compat shim. See ``goconnect.land.providers.geotab``."""


try:
    from goconnect.land.providers.geotab import *  # noqa: F401,F403
    from goconnect.land.providers.geotab import GeotabProvider  # noqa: F401
except ModuleNotFoundError:
    pass
