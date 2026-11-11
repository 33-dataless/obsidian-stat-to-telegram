from apscheduler.schedulers.background import BackgroundScheduler


class Planner:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def create_task(
        self,
        task,
        type="cron",
        hour=8,
        minute=0,
        args=None,
        kwargs=None,
    ):
        self.scheduler.add_job(
            task,
            type,
            hour=hour,
            minute=minute,
            args=args or [],
            kwargs=kwargs or {},
        )

    def start_planner(self):
        self.scheduler.start()

    def stop_planner(self):
        self.scheduler.shutdown()