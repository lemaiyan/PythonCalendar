__author__ = '@author'

from PythonCalendar.ScheduleConflictError import *


class EventPlanner:

    def __init__(self, owner, events=None):
        """
        Constructor
        :param owner:
        :param events:
        :return:
        """
        self.owner = owner
        if events is None:
            self.events = []
        else:
            self.events = events

    def __str__(self):
        return "EventPlanner (\"{0}\", {1})".format(self.owner, self.events)

    def __repr__(self):
        return str(self)

    def add_event(self, event):
        """
        Add the given event
        :param event:
        :return:
        """
        # check whether there is any events so the list

        if len(self.events) == 0:
            self.events.append(event)
            return None
        else:
            for ev in self.events:
                if ev.timespan.overlaps(event.timespan):
                    raise ScheduleConflictError("The event {0}, overlaps with event {1}".format(event, ev))

            # if we get here then that means there is no overlap so we add the event
            self.events.append(event)
            return None

    def add_events(self, events):
        """
        Adds events in the given list
        :param events:
        :return:
        """
        events_not_added = 0
        length = len(events)

        if length == 0:
            return 0
        else:
            for i in range(0, length):
                ev = events.pop()
                try:
                    self.add_event(ev)
                except ScheduleConflictError as ex:
                    events_not_added += 1
            return events_not_added

    def available_at(self, moment):
        """
        Checks if the owner is available at the given mat
        :param moment:
        :return:
        """
        if len(self.events) == 0:
            return True
        else:
            for ev in self.events:
                if ev.timespan.during_moment(moment):
                    return False
            return True

    def available_during(self, timespan):
        """
        Checks if the owner is available at the given timespan
        :param timespan:
        :return:
        """
        if len(self.events) == 0:
            return True
        else:
            for ev in self.events:
                if ev.timespan.overlaps(timespan):
                    return False
            return True

    def can_attend(self, event):
        """
        Checks if the owner can attend the event
        :param event:
        :return:
        """
        if len(self.events) == 0:
            return True
        else:
            # make sure the User is not available during that event
            return not self.available_during(event.timespan)

# Here we run a test program

if __name__ == '__main__':
    # welcome
    print("Hello User, Welcome to the Python Calendar")
    input("Select \n1. To add an Event.\n2. To add events\n")

