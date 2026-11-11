from config import configure_logger, config
from manager import Manager
from planner import Planner
import time

def task(manager: Manager):
    manager.commit()


def main() -> None:
    configure_logger()

    manager = Manager(
        path=config._OBSIDIAN_PATH,
        url=config._SERVER_URL
    )
    
    planner = Planner()

    planner.create_task(
        task=task,
        type="cron",
        hour=8,
        minute=0,
        kwargs={"manager": manager},
    )

    planner.start_planner()


if __name__ == "__main__":
    main()
    