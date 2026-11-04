from config import configure_logger, get_path
from scanner import Scanner
import time

def main() -> None:
    configure_logger()
    path = get_path()

    scanner = Scanner(
        path=path,
        recursive=True
    )
    
    observer = scanner.registrate_observer()
    observer.start()
    
    try:
        while True:
            time.sleep(1)
            print('scanning...')
    finally:
        observer.stop()
        observer.join()
        
if __name__ == "__main__":
    main()
    