import math

class Clock:
    def __init__(self, hour, minute):
        extra_hours = math.floor(minute / 60)
        self.hour = (hour + extra_hours) % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        hours = math.floor(total_minutes / 60)
        minutes = total_minutes % 60
        self.hour += hours
        self.minute = minutes
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes
        hours = math.floor(total_minutes / 60)
        minutes = total_minutes % 60
        self.hour += hours
        self.minute = minutes
        return Clock(self.hour, self.minute)
