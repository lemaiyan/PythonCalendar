__author__ = '@author'
from PythonCalendar.Moment import *
from PythonCalendar.TimeError import *


class TimeSpan:

    def __init__(self, start, stop):
        """
        Constructor
        :param start:
        :param stop:
        :return:
        """
        if stop.before(start):
            raise TimeError("The stop moment {0} cannot be before start moment {1}".format(stop, start))
        else:
            self.start = start
            self.stop = stop

    def __str__(self):
        return "Timespan({0}, {1})".format(self.start, self.stop)

    def __repr__(self):
        return "Timespan({0}, {1})".format(repr(self.start), repr(self.stop))

    def during_moment(self, moment):
        """
        Checks if the moment is during the timespan
        :param moment:
        :return:
        """

        if self.start.before(moment) and self.stop.after(moment):
            return True
        elif self.start.equal(moment) or self.stop.equal(moment):
            return True
        else:
            return False

    def overlaps(self, other):
        """
        Checks if the Time spans overlaps
        :param other:
        :return:
        """

        if self.start.equal(other.start) or self.stop.equal(other.stop):
            return True
        elif self.start.before(other.start) and self.stop.after(other.start):
            return True
        elif other.stop.after(self.start) and other.stop.before(self.stop):
            return True
        else:
            return False

    def set_duration(self, year=0, month=0, day=0, hour=0, minute=0):
        """
        Resets ths values of the stop moment
        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :return:
        """
        self.stop.delta(year, month, day, hour, minute)
        if self.stop.before(self.start):
            raise TimeError("The stop Moment is before the start Moment")
        else:
            return True


