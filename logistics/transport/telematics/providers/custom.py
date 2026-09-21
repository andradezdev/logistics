"""Compat shim. See ``goconnect.land.providers.custom``."""


try:
    from goconnect.land.providers.custom import *  # noqa: F401,F403
    from goconnect.land.providers.custom import CustomProvider  # noqa: F401
except ModuleNotFoundError:
    pass
