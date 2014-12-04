__author__ = '@author'
import unittest
from PythonCalendar.Moment import *


class AllTests (unittest.TestCase):
    # first test case.
    def test1(self):
        """check that Moment constructor assigns each instance variable correctly."""

        # create a Moment object
        m = Moment(2014, 12, 12, 7, 30)

        # Check if the results are as expected
        self.assertEqual(m.year, 2014)
        self.assertEqual(m.month,   12)
        self.assertEqual(m.day,   12)
        self.assertEqual(m.hour,    7)
        self.assertEqual(m.minute,   30)

        # second test case.
    def test2(self):
        """check Moment's .before() definition (decided by year)"""
        m1 = Moment(2013,  5, 10, 5, 25)
        m2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(m1.before(m2))

    def test3(self):
        """check Moment's .after() definition (decided by year)"""
        m1 = Moment(2013,  5, 10, 5, 25)
        m2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(m2.after(m1))

    def test4(self):
        """check Moment's .equal() definition (decided by all the parameters)"""
        m1 = Moment(2014,  12, 12, 7, 30)
        m2 = Moment(2014, 12, 12, 7, 30)
        self.assertTrue(m1.equal(m2))

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
