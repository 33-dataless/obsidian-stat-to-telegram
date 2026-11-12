from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from logging import getLogger

log = getLogger(__name__)

class EventHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        log.debug("file modified")
        self._handle(event)

    def on_created(self, event):
        log.debug("file created")
        self._handle(event)

    def on_deleted(self, event):
        log.debug("file deleted")
        self._handle(event)

    def on_moved(self, event):
        log.debug("file moved")
        self._handle(event)

    def _handle(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".md"):
            self.callback(event)


class Scanner:
    def __init__(self, path, callback, recursive=True):
        self.path = path
        self.recursive = recursive

        self.event_handlers = EventHandler(callback)

    def registrate_observer(self):
        observer = Observer()

        observer.schedule(
            self.event_handlers,
            path=self.path,
            recursive=self.recursive
        )

        return observer