from config import config
from manager import Manager
from logger import configure_logger
import time

def task(manager: Manager):
    manager.commit()


def main() -> None:
    configure_logger()

    manager = Manager(
        path=config._OBSIDIAN_PATH,
        url=config._SERVER_URL
    )

    manager.start()

    try:
        while True:
            import time
            time.sleep(1)
            print("wait change")
    except KeyboardInterrupt:
        manager.stop()
    


if __name__ == "__main__":
    main()
    