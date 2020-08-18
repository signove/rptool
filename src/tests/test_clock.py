import unittest

import time
from core.clock import Clock


class TestClock(unittest.TestCase):

    def test_clock_start_with_zero(self):
        """ Test if the clock starts counting from zero. """
        clock = Clock()
        clock.start()
        self.assertTrue(clock.getTime() == 0, "Expected clock counting zero when starts!")

    def test_clock_get_time(self):
        """ Test if the clock is started """
        clock = Clock()
        clock.start()
        time.sleep(1)
        self.assertFalse(clock.getTime() == 1, "Expected be counting 1 second!")

    def test_clock_should_count_time_between_start_and_stop(self):
        """ Test if is counting the time elapsed after start until stop. """
        clock = Clock()
        clock.start()
        time.sleep(1)
        clock.stop()
        self.assertTrue(clock.getTime() == 1, "Expected time be 1s")
        clock.start()
        time.sleep(2)
        clock.stop()
        print(clock.getTime())
        self.assertTrue(clock.getTime() == 2, "Expected time be 2s")


if __name__ == '__main__':
    unittest.main()
