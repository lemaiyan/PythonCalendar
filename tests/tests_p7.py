__author__ = '@author'
import unittest
from PythonCalendar.Moment import *
from PythonCalendar.TimeSpan import *
from PythonCalendar.Event import *
from PythonCalendar.EventPlanner import *


class AllTests (unittest.TestCase):
    # ---------------------------------------------#
    #               Moment Tests                   #
    # ---------------------------------------------#
    def test1(self):
        """check that Moment constructor assigns each instance variable correctly."""

        # create a Moment object
        moment = Moment(2014, 12, 12, 7, 30)

        # Check if the results are as expected
        self.assertEqual(moment.year, 2014)
        self.assertEqual(moment.month,   12)
        self.assertEqual(moment.day,   12)
        self.assertEqual(moment.hour,    7)
        self.assertEqual(moment.minute,   30)

    def test2(self):
        """check that Moment constructor throws a TimeError"""
        try:
            m = Moment(2014, 12, 12, 7, -1)
        except Exception as ex:
            self.assertIsInstance(ex, TimeError)

    def test3(self):
        """check Moment's .before() definition (decided by year)"""
        moment1 = Moment(2013,  5, 10, 5, 25)
        moment2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(moment1.before(moment2))

    def test4(self):
        """check Moment's .after() definition (decided by year)"""
        m1 = Moment(2013,  5, 10, 5, 25)
        m2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(m2.after(m1))

    def test5(self):
        """check Moment's .equal() definition (decided by all the parameters)"""
        m1 = Moment(2014,  12, 12, 7, 30)
        m2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(m1.equal(m2))

    def test6(self):
        """check Moment's .delta() definition (decided by minutes the smallest unit)"""
        m = Moment(2014, 12, 31, 23, 00)
        m.delta(0, 0, 0, 0, 72)

        # Check if the results are as expected
        self.assertEqual(m.year, 2015)
        self.assertEqual(m.month,   1)
        self.assertEqual(m.day,   1)
        self.assertEqual(m.hour,    0)
        self.assertEqual(m.minute,   12)

    # ---------------------------------------------#
    #               Timespan Tests                 #
    # ---------------------------------------------#

    def test7(self):
        """check that Timespan constructor assigns each instance variable correctly."""
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)

        span = TimeSpan(start, stop)

        # check if the results are as expected
        self.assertTrue(span.start.equal(start))
        self.assertTrue(span.stop.equal(stop))

    def test8(self):
        """check Moment's .during_moment() definition (decided by minutes the smallest unit)"""
        start = Moment(2014,  12, 10, 0, 0)
        stop = Moment(2014, 12, 12, 0, 0)
        span = TimeSpan(start, stop)

        # check if the results are as expected
        self.assertTrue(span.during_moment(start))

    def test9(self):
        """check Moment's .overlaps() definition (decided by minutes the smallest unit)"""
        start = Moment(2014,  11, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        m = Moment(2014,  10, 12, 7, 25)
        m2 = Moment(2014,  11, 9, 7, 25)
        span = TimeSpan(start, stop)
        span2 = TimeSpan(m, m2)
        # check if the results are as expected
        self.assertFalse(span.overlaps(span2))

    def test10(self):
        """check that Timespan .set_duration() (decided by minutes the smallest unit)"""
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)

        span = TimeSpan(start, stop)
        span.set_duration(0, 0, 0, 0, 30)
        # check if the results are as expected
        # Check if the results are as expected
        self.assertEqual(span.stop.year, 2014)
        self.assertEqual(span.stop.month,   12)
        self.assertEqual(span.stop.day,   12)
        self.assertEqual(span.stop.hour,    8)
        self.assertEqual(span.stop.minute,   0)

    def test11(self):
        """check that Timespan .set_duration() thro"""
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)

        span = TimeSpan(start, stop)
        span.set_duration(0, 0, 0, 0, 30)
        # check if the results are as expected
        # Check if the results are as expected
        self.assertEqual(span.stop.year, 2014)
        self.assertEqual(span.stop.month,   12)
        self.assertEqual(span.stop.day,   12)
        self.assertEqual(span.stop.hour,    8)
        self.assertEqual(span.stop.minute,   0)

    # ---------------------------------------------#
    #               Event Tests                    #
    # ---------------------------------------------#

    def test12(self):
        """check that Event constructor assigns each instance variable correctly."""
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)

        span = TimeSpan(start, stop)

        event = Event("Lunch With Mum", "Home", span)

        # check if the values are as expected
        self.assertEqual(event.location, "Home")
        self.assertEqual(event.title, "Lunch With Mum")
        self.assertTrue(event.timespan.start.equal(start))
        self.assertTrue(event.timespan.stop.equal(stop))

    # ---------------------------------------------#
    #               EventPlanner Tests             #
    # ---------------------------------------------#

    def test13(self):
        """check that EventPlanner constructor assigns each instance variable correctly."""
        event_planner = EventPlanner("Owner")

        # check if the values are as expected
        self.assertEqual(event_planner.owner, "Owner")
        self.assertEqual(event_planner.events, [])  # empty list of events

    def test14(self):
        """check that EventPlanner .add_event() """
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        event = Event("Lunch With Mum", "Home", span)
        event_planner = EventPlanner("Owner")
        event_planner.add_event(event)

        # check if we are getting the expected values
        self.assertEqual(event_planner.owner, "Owner")
        self.assertEqual(len(event_planner.events), 1)  # to make sure we only have on item in the event list

    def test15(self):
        """check that EventPlanner .add_events() """
        start = Moment(2013,  5, 10, 5, 25)
        start2 = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2013, 12, 12, 7, 30)
        stop2 = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        span2 = TimeSpan(start2, stop2)
        event = Event("Lunch With Mum", "Home", span)
        event2 = Event("Lunch With Mum", "Restaurant", span2)
        events = [event, event2]
        event_planner = EventPlanner("Owner")
        event_planner.add_events(events)

        # check if we are getting the expected values
        self.assertEqual(event_planner.owner, "Owner")
        self.assertEqual(len(event_planner.events), 2)  # to make sure we only have on item in the event list

    def test16(self):
        """check that EventPlanner .available_at() """
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        event = Event("Lunch With Mum", "Home", span)
        event_planner = EventPlanner("Owner")
        event_planner.add_event(event)

        # check if we get the expected value
        self.assertFalse(event_planner.available_at(start))

    def test15(self):
        """check that EventPlanner .available_during() """
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        event = Event("Lunch With Mum", "Home", span)
        event_planner = EventPlanner("Owner")
        event_planner.add_event(event)

        # check if we get the expected value
        self.assertFalse(event_planner.available_during(span))

    def test117(self):
        """check that EventPlanner .available_during() """
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        event = Event("Lunch With Mum", "Home", span)
        event_planner = EventPlanner("Owner")
        event_planner.add_event(event)

        # check if we get the expected value
        self.assertFalse(event_planner.available_during(span))

    def test118(self):
        """check that EventPlanner .can_attend() """
        start = Moment(2014,  5, 10, 5, 25)
        stop = Moment(2014, 12, 12, 7, 30)
        span = TimeSpan(start, stop)
        event = Event("Lunch With Mum", "Home", span)
        event_planner = EventPlanner("Owner")
        event_planner.add_event(event)

        # check if we get the expected value

        self.assertTrue(event_planner.can_attend(event))

# ---------------------------------------------#
# we have to manually turn those methods into  #
# formal test cases, grouped as a TestSuite.   #
# ---------------------------------------------#

# some ugly code that counts how many testX
# functions you've added, automatically.
num_tests = len(list(AllTests.__dict__)) - 2


class TheTestSuite (unittest.TestSuite):
    # constructor.
    def __init__(self):
        # collect a sequence of tests in a list.
        fs = []
        fs.extend(map(lambda n: AllTests("test"+str(n)), range(1, num_tests+1)))
        # call parent class's constructor.
        unittest.TestSuite.__init__(self, fs)

# ---------------------------------------------#
#  finally, we can run the tests all together. #
# ---------------------------------------------#

# create an object that can run tests.
runner = unittest.TextTestRunner()

# define the suite of tests that should be run.
suite1 = TheTestSuite()

# let the runner run the suite of tests.
runner.run(suite1)
