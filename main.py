from config import config
from manager import Manager
from logger import configure_logger
from logging import getLogger
import time

log = getLogger(__name__)

def main() -> None:
    configure_logger()

    manager = Manager(
        path=config._OBSIDIAN_PATH,
        url=config._SERVER_URL
    )

    manager.start()
    log.info('~ application start')
    try:
        while True:
            time.sleep(1)
            log.info("...")
    except KeyboardInterrupt:
        manager.stop()
    
if __name__ == "__main__":
    main()
    