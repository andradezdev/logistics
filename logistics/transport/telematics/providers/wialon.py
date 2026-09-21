"""Compat shim. See ``goconnect.land.providers.wialon``."""


try:
    from goconnect.land.providers.wialon import *  # noqa: F401,F403
    from goconnect.land.providers.wialon import WialonProvider  # noqa: F401
except ModuleNotFoundError:
    pass
