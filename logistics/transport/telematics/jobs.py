"""Compat shim. See ``goconnect.land.jobs``."""


try:
    from goconnect.land.jobs import *  # noqa: F401,F403
    from goconnect.land.jobs import tick  # noqa: F401
except ModuleNotFoundError:
    pass
