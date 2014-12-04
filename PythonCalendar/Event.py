__author__ = '@author'

from PythonCalendar.TimeSpan import *
from PythonCalendar.Moment import *


class Event:

    def __init__(self, title, location, timespan):
        """
        Constructor
        :param title:
        :param location:
        :param timespan:
        :return:
        """
        self.title = title
        self.location = location
        self.timespan = timespan

    def __str__(self):
        return "Event: {0}. Location: {1}. {2}, {3} ".format(self.title, self.location, self.timespan.start, self.timespan.stop)

    def __repr__(self):
        return "Event (\"{0}\", \"{1}\", {2})".format(self.title, self.location, repr(self.timespan))


if __name__ == '__main__':
    start = Moment(2014, 12, 4, 14, 1)
    stop = Moment(2014, 12, 4, 14, 30)
    span = TimeSpan(start, stop)
    e = Event("Lunch With Mum", "Home", span)
    print(e)
    print(repr(e))