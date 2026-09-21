"""Compat shim. See ``goconnect.land.providers.samsara``."""


try:
    from goconnect.land.providers.samsara import *  # noqa: F401,F403
    from goconnect.land.providers.samsara import SamsaraProvider  # noqa: F401
except ModuleNotFoundError:
    pass
