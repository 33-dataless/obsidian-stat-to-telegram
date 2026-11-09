from apscheduler.schedulers.background import BackgroundScheduler

class Planner:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def create_task(self, task, type="cron", hour=8, minute=0):
        self.scheduler.add_job(task, type)

    def start_planner(self):
        self.scheduler.start()

    def stop_planner(self):
        self.scheduler.shutdown()
        
