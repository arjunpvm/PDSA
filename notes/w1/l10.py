# TIMER

import time


class TimeError(Exception):
    """A custom exception to report errors of the Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def start(self):
        if self._start_time is not None:
            raise TimeError(
                "Timer already started. Please stop it to start again")
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimeError("Please start the timer first")
        self._stop_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed_time(self):
        if self._start_time is None:
            raise TimeError("please start the timer first")
        return self._stop_time

    def __str__(self):
        return str(self._stop_time)


t = Timer()


for i in range(4, 9):
    t.start()
    n = 0
    for j in range(10**i):
        n += j
    t.stop()

    print(i, t)


# this prints the time taken to execute the loop for 10^4 to 10^8
