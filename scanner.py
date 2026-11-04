from watchdog import events
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time

logger = logging.getLogger(__name__)

class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(
            f"Type: {event.event_type}",
            f"Path: {event.src_path}",
            f"Is directory: {event.is_directory}"
        )

    def on_created(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_changed(self, event):
        pass
    

class Scanner():
    def __init__(self, path, recursive=True):
        self.__path__ = path
        self.__recursive__ = recursive
        self.__event_handlers__ = EventHandler()

    def registrate_observer(self):
        observer = Observer()
        if self.__path__:
            observer.schedule(
                self.__event_handlers__,
                path=self.__path__,
                recursive=self.__recursive__
            )
        return observer
        
    def get_path(self):
        return self.__path__
    


    
        
