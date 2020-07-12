# -*- coding: utf-8 -*-
import time


class Clock:

    def __init__(self):
        self.time = time.time()
        self._start = 0
        self._end = 0
        self._elapsed = 0

    def start(self):
        if self._start == 0:
            self._start = time.time()
        else:
            self.stop()

    def stop(self):
        self._end = time.time()
        self._elapsed = (self._end - self._start)
        self._start = self._end

    def getTime(self):
        return round(self._elapsed, 2)