# TIMING OUR CODE

import time

start = time.perf_counter()

# execute code

end = time.perf_counter()

elapsed_time = end - start

# lets do this using class


class Timer:
    def __init__(self):
        self._start_time = 0
        self._stop_time = 0

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        self._stop_time = time.perf_counter() - self._start_time

    def elapsed_time(self):
        return self._stop_time
