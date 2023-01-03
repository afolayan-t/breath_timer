import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class BreathTimer:
    """The purpose of this project is to let me do the breathing excercise outlined in the book Breath by James Nestor."""
    def __init__(self, length:int=0):
        """
        Length of time in seconds to run. Will do 5.5 second inhales and 5.5 second exhales
        """

        self._start_time = None
        self.end_time = length if length else 360

    def run(self) -> None:
        inhale = True
        if self._start_time is not None:
            raise TimerError(f"Timer is not running. Use .stop() to stop it")

        print("*"*20 + "\n\n")

        self._start_time = time.perf_counter()
        counter = 0
        while (time.perf_counter() - self._start_time) < self.end_time:
            curr_epoch = (time.perf_counter() - self._start_time) # how much time has currently passed
            cycle = abs(curr_epoch - counter*5.5) # current cycle from 0 to 5.5 

            if cycle > 5.5:
                if inhale:
                    print("Inhale...\n\n")
                else:
                    print("Now Exhale...\n\n")
                print("*"*20 + "\n\n")
                # print("5.5 seconds have passed")
                counter += 1
                inhale = not inhale


        print("We are done, the time has elapsed.\n")
        print("This timer was inspired by the Book Breath: The New Science of a Lost Art Hardcover by James Nestor.\nSuggesting that inhales and exhales of 5.5 seconds is the optimum amount of time for breathing.")
        print("if you want to check out James Nestor's book use the link here; https://a.co/d/fDpfxxc")
        return

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is not running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. USe .start() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")