from config import configure_logger, get_path
from scanner import Scanner
from snapshot import Snapshot

import time

def main() -> None:
    configure_logger()
    path = get_path()
    snapshot = Snapshot(path=path)
    current_snapshot = snapshot.create_snapshot()

    for key, value in current_snapshot.items():
        print(key, value)

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
    