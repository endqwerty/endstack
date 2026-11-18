import random
import threading
import time

__all__ = ["Notifier"]


class Notifier:
    def __init__(self, deliver):
        self._deliver = deliver

    def send(self, message):
        def work():
            time.sleep(random.uniform(0, 0.08))
            self._deliver(message.strip())

        thread = threading.Thread(target=work)
        thread.start()
        return thread
