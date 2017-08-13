from unittest import TestCase
from datetimedelta.extended_date_time import ExtendedDateTime
from datetime import datetime
from dateutil.relativedelta import relativedelta


class TestExtendedDateTime(TestCase):

    # Check whether instance is of type Date time
    def test_instance_type(self):
        extend_date_time_obj = ExtendedDateTime(2)
        self.assertIsInstance(extend_date_time_obj.days.ago, datetime)

    # Check whether Days.ago & Days.After are evaluated correctly
    def test_days_ago_delta(self):
        days_gap = ExtendedDateTime(2)

        current_date = datetime.now().date()
        delta = relativedelta(days=-2)
        expected_date = current_date + delta
        calculated_date = days_gap.days.ago.date()

        self.assertEqual(calculated_date, expected_date)

    def test_days_after_delta(self):
        days_gap = ExtendedDateTime(2)

        current_date = datetime.now().date()
        delta = relativedelta(days=2)
        expected_date = current_date + delta
        calculated_date = days_gap.days.after.date()

        self.assertEqual(calculated_date, expected_date)

    # Check whether Weeks.ago & Weeks.after are evaluated correctly
    def test_weeks_ago_delta(self):
        weeks_gap = ExtendedDateTime(3)

        current_date = datetime.now().date()
        delta = relativedelta(weeks=-3)
        expected_date = current_date + delta
        calculated_date = weeks_gap.weeks.ago.date()

        self.assertEqual(calculated_date, expected_date)

    def test_weeks_after_delta(self):
        weeks_gap = ExtendedDateTime(3)

        current_date = datetime.now().date()
        delta = relativedelta(weeks=3)
        expected_date = current_date + delta
        calculated_date = weeks_gap.weeks.after.date()

        self.assertEqual(calculated_date, expected_date)

    # Check whether Months.ago & Months.after are evaluated correctly
    def test_months_ago_delta(self):
        months_gap = ExtendedDateTime(4)

        current_date = datetime.now().date()
        delta = relativedelta(months=-4)
        expected_date = current_date + delta
        calculated_date = months_gap.months.ago.date()

        self.assertEqual(calculated_date, expected_date)

    def test_months_after_delta(self):
        months_gap = ExtendedDateTime(4)

        current_date = datetime.now().date()
        delta = relativedelta(months=4)
        expected_date = current_date + delta
        calculated_date = months_gap.months.after.date()

        self.assertEqual(calculated_date, expected_date)

    # Check whether Years.ago & Years.after are evaluated correctly
    def test_years_ago_delta(self):
        years_gap = ExtendedDateTime(1)

        current_date = datetime.now().date()
        delta = relativedelta(years=-1)
        expected_date = current_date + delta
        calculated_date = years_gap.years.ago.date()

        self.assertEqual(calculated_date, expected_date)

    def test_years_after_delta(self):
        years_gap = ExtendedDateTime(1)

        current_date = datetime.now().date()
        delta = relativedelta(years=1)
        expected_date = current_date + delta
        calculated_date = years_gap.years.after.date()

        self.assertEqual(calculated_date, expected_date)

    # Check whether proper exceptions raised for no days, weeks, months given
    def test_no_delta_type_ago_exception(self):
        extend_date_time_obj = ExtendedDateTime(2)
        with self.assertRaises(Exception) as context:
            extend_date_time_obj.ago

        self.assertTrue('Need days or weeks or months or years to compute datetime delta',
            str(context.exception))

    def test_no_delta_type_after_exception(self):
        extend_date_time_obj = ExtendedDateTime(2)
        with self.assertRaises(Exception) as context:
            extend_date_time_obj.after

        self.assertTrue('Need days or weeks or months or years to compute datetime delta',
            str(context.exception))
