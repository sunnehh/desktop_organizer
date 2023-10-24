"""
@author: sunny
"""
import time
import os
import shutil
import re
import watchdog
import watchdog.events


class Watch_desktop:
    def __init__(self) -> None:
        self._observer = watchdog.observers.Observer()

    def start(self) -> None:
        self._observer.schedule(event_handler, source_dir, recursive=True)
        self._observer.start()

        try:
            while True:
                time.sleep(100)
        except:
            self._observer.stop()
            print("Desktop watcher stopped")


class File_handler(watchdog.events.FileSystemEventHandler):
    """Extends FileSystemEventHandler"""

    def on_any_event(self, event: watchdog.events.FileSystemEvent):
        """Overloads the on_any_event method and watches for any file system event
        https://pythonhosted.org/watchdog/api.html
        """
        if event.is_directory:
            pass

    # using static method decorator because the method is logically related
    # to the file handler class, but does not depend on any instance-specific attributes
    @staticmethod
    def move_file(file, source):
        pass


if __name__ == "__main__":
    pass
