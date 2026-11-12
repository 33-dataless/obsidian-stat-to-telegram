from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class EventHandler(FileSystemEventHandler):

    def __init__(self, callback):
        self.callback = callback

    def on_modified(self, event):
        self._handle(event)

    def on_created(self, event):
        self._handle(event)

    def on_deleted(self, event):
        self._handle(event)

    def on_moved(self, event):
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