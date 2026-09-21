"""Compat shim. See ``goconnect.land.ingest``."""


try:
    from goconnect.land.ingest import *  # noqa: F401,F403
    from goconnect.land.ingest import run_ingest  # noqa: F401
except ModuleNotFoundError:
    pass
