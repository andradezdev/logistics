"""Compat shim. See ``goconnect.land.providers``."""


try:
    from goconnect.land.providers import *  # noqa: F401,F403
    from goconnect.land.providers import make_provider  # noqa: F401
except ModuleNotFoundError:
    pass
