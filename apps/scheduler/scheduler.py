from apscheduler.schedulers.asyncio import AsyncIOScheduler

from apps.scheduler.jobs import run_ingestion_job

scheduler = AsyncIOScheduler()


def start_scheduler():
    """
    Start background jobs.
    """

    scheduler.add_job(
        run_ingestion_job,
        "interval",
        hours=1,
    )

    scheduler.start()
