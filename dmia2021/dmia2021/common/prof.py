import logging
import time

from typing import Any, Dict

logger = logging.getLogger(__name__)


class TimedContext:
    def __init__(self, name: str, time_storage: Dict[str, Any]):
        self.name = name
        self.time_storage = time_storage
        self.enter_time = None

    def __enter__(self):
        self.enter_time = time.time()
        return self

    def __exit__(self, *args):
        if self.name not in self.time_storage:
            self.time_storage[self.name] = 0
        self.time_storage[self.name] += time.time() - self.enter_time
