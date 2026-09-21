"""Compat shim. See ``goconnect.flight.tasks``.

These cron entry points are now registered by ``goconnect/hooks.py``; the
re-exports below keep any direct ``frappe.call`` / ``bench execute`` paths
in ``logistics`` working without touching individual call sites.
"""

try:
    from goconnect.flight.tasks import *  # noqa: F401,F403
    from goconnect.flight.tasks import (  # noqa: F401
        cleanup_old_schedules,
        cleanup_old_sync_logs,
        sync_active_flights,
        sync_airline_master,
        sync_airport_master,
        sync_route_data,
        update_air_freight_jobs_with_flight_status,
    )
except ModuleNotFoundError:
    def cleanup_old_schedules(*args, **kwargs):
        pass

    def cleanup_old_sync_logs(*args, **kwargs):
        pass

    def sync_active_flights(*args, **kwargs):
        pass

    def sync_airline_master(*args, **kwargs):
        pass

    def sync_airport_master(*args, **kwargs):
        pass

    def sync_route_data(*args, **kwargs):
        pass

    def update_air_freight_jobs_with_flight_status(*args, **kwargs):
        pass
