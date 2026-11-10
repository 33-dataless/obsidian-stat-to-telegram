from config import configure_logger, config
from manager import Manager
import time

def main() -> None:
    configure_logger()
    manager = Manager(
        path = config._OBSIDIAN_PATH
    )
    manager.start()



    # scanner = Scanner(
    #     path=path,
    #     recursive=True
    # )
    
    # observer = scanner.registrate_observer()
    # observer.start()
    
    # try:
    #     while True:
    #         time.sleep(1)
    # finally:
    #     observer.stop()
    #     observer.join()
        
if __name__ == "__main__":
    main()
    