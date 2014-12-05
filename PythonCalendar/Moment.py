__author__ = '@author'

from PythonCalendar.TimeError import *


class Moment():

    def __init__(self, year=0, month=0, day=0, hour=0, minute=0):
        """
        Constructor
        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :return:
        """
        try:
            if Moment.is_int("Year", year) and Moment.is_int("Month", month) and Moment.is_int("Day", day) \
                    and Moment.is_int("Hour", hour) and Moment.is_int("Minute", minute):
                if Moment.is_year_valid(year):
                    self.year = year
                if Moment.is_month_valid(month):
                    self.month = month
                if Moment.is_day_valid(year, month, day):
                    self.day = day
                if Moment.is_hour_valid(hour):
                    self.hour = hour
                if Moment.is_minute_valid(minute):
                    self.minute = minute

        except Exception as e:
            print(e)

    def __str__(self):
        fmonth = self.month
        fday = self.day
        fhour = self.hour
        fminute = self.minute
        if self.month < 10:
            fmonth = "0{0}".format(self.month)
        if self.day < 10:
            fday = "0{0}".format(self.day)
        if self.hour < 10:
            fhour = "0{0}".format(self.hour)
        if self.minute < 10:
            fminute = "0{0}".format(self.minute)

        return "{0}/{1}/{2}-{3}:{4}".format(self.year, fmonth, fday, fhour, fminute)

    def __repr__(self):
        return "Moment({0}, {1}, {2}, {3}, {4})".format(self.year, self.month, self.day, self.hour, self.minute)

    def before(self, other):
        """
        Checks if the Moment is before other
        :param other:
        :return:
        """

        if self.year < other.year:

            return True
        else:
            if self.month < other.month and self.year < other.year:

                return True
            else:
                if self.day < other.day and (self.month < other.month and self.year < other.year):

                    return True
                else:
                    if self.hour < other.hour and (self.day < other.day and self.month < other.month and self.year < other.year):
                        return True
                    else:
                        if self.minute < other.minute and (self.hour < other.hour and self.day < other.day and self.month < other.month and self.year < other.year):

                            return True
                        else:
                            return False

    def equal(self, other):
        """
        Checks if the two moments are equal
        :param other:
        :return:
        """
        is_equal = False
        if self.year == other.year:
            is_equal = True
            if self.month == other.month:
                is_equal = True
                if self.day == other.day:
                    is_equal = True
                    if self.hour == other.hour:
                        is_equal = True
                        if self.minute == other.minute:
                            is_equal = True
                        else:
                            is_equal = False
                    else:
                        is_equal = False
                else:
                    is_equal = False
            else:
                is_equal = False
        else:
            is_equal = False

        return is_equal

    def after(self, other):
        """
        Checks is the moment is after the other
        :param other:
        :return:
        """
        is_early = False
        if self.year > other.year:
            is_early = True
        else:
            if self.month > other.month and self.year > other.year:
                is_early = True
            else:
                if self.day > other.day and (self.month > other.month and self.year > other.year):
                    is_early = True
                else:
                    if self.hour > other.hour and (self.day > other.day and self.month > other.month and self.year > other.year):
                        is_early = True
                    else:
                        if self.minute > other.minute and (self.hour > other.hour and self.day > other.day and self.month > other.month and self.year > other.year):
                            is_early = True
                        else:
                            is_early = False
        return is_early

    def delta(self, year=0, month=0, day=0, hour=0, minute=0):
        """
        Transforms the current moment in a positive or negative way
        :param year:
        :param month:
        :param day:
        :param hour:
        :param minute:
        :return:
        """

        # first check if the deal with the minutes
        carry_over_hours = int((self.minute + minute) / 60)
        new_minutes = (self.minute + minute) % 60

        #then deal with the hours
        carry_over_days = int((self.hour + hour + carry_over_hours) / 24)
        new_hours = (self.hour + hour + carry_over_hours) % 24

        #deal with days

        remaining_days_to_end_of_the_current_month = Moment.get_number_of_days_in_a_month(self.year, self.month)- (self.day + carry_over_days)

        #check if the days we have overflow

        overflow_days = day - remaining_days_to_end_of_the_current_month
        #if the overflow_days are 0 or negative then we good we end there else we loop through the days until they are done

        new_month = 0
        carry_over_months = 0
        new_day = 0
        new_year = 0
        if overflow_days <= 0:
            new_day = self.day + day + carry_over_days
            new_month = self.month
            carry_over_months = 0
            overflow_days = 0
        else:
            carry_over_months += 1
            new_month = self.month + 1
            new_year = self.year
            while overflow_days > 0:
                if new_month == 13:
                    new_month = 1
                    new_year += 1
                month_length = Moment.get_number_of_days_in_a_month(new_year, new_month)
                overflow = overflow_days - month_length
                if overflow < 0:
                    #here we remain in the same month
                    new_day = overflow_days
                    overflow_days = 0
                elif overflow == 0:
                    #here we remain in the same month and set the day to the last day of the month
                    new_day = month_length
                    overflow_days = 0
                elif overflow > 0:
                    carry_over_months += 1
                    new_month += 1
                    overflow_days = overflow

        #now we deal with the months

        carry_over_years = 0
        if (self.month + month + carry_over_months) % 12 == 0:
            new_month = 12
        else:
            new_month = (self.month + month + carry_over_months) % 12
            carry_over_years = int((self.month + month + carry_over_months) / 12)

        # dealing with years

        new_year = self.year + carry_over_years + year

        #bringing everything together

        self.year = round(new_year)
        self.month = round(new_month)
        self.day = round(new_day)
        self.hour = round(new_hours)
        self.minute = round(new_minutes)

    def is_leap_year(year):
        """
        Checks if the year is leap year
        :param year:
        :return: Boolean either true or false
        """
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def is_int(name, value):
        """
        Checks if the value provided is int
        :param name:
        :param value:
        :return:
        """
        if isinstance(value, int):
            return True
        else:
            raise TimeError("The value provided for %s is not an integer" % name)

    def is_year_valid(year):
        if year >= 0:
            return True
        else:
            raise TimeError("The value {0} provided for year is not valid".format(year))

    def is_month_valid(month):
        """
        Checks if the month is valid
        :param month:
        :return:
        """
        if month >= 1 and month <= 12:
            return True
        else:
            raise TimeError("The value {0} provided for month is not valid".format(month))

    def is_day_valid(year, month, day):
        """
        Checks if the day passed is valid
        :param year:
        :param month:
        :param day:
        :return:
        """
        start_day = 1
        last_day = 0

        #first we determine the last day of the month

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            last_day = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            last_day = 30
        else:
            if Moment.is_leap_year(year):
                last_day = 29
            else:
                last_day = 28

        #then we check if they day of the month is valid
        if day >= start_day and day <= last_day:
            return True
        else:
            raise TimeError("The value {0} for day of {1} month and {2} year is not valid".format(
                day, month, year))


    def is_hour_valid(hour):
        if hour >=0 and hour <=23:
            return True
        else:
            raise TimeError("The value {0} provided for hour is not valid".format(hour))

    def is_minute_valid(minute):
        if minute >= 0 and minute <= 59:
            return True
        else:
            raise TimeError("The value {0} provided for minute is not valid".format(minute))

    def get_number_of_days_in_a_month(year, month):
        days_in_a_month = 0
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days_in_a_month = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days_in_a_month = 30
        else:
            if Moment.is_leap_year(year):
                days_in_a_month = 29
            else:
                days_in_a_month = 28

        return days_in_a_month


