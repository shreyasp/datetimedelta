#!/usr/bin/python3
# This module gives extended functionality for calculating datetime based on
# functionality that exists in Ruby
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


class ExtendedDateTime(int):
    STANDARD_ATTRS = ['_calc_day', '_calc_week', '_calc_month']

    def __new__(cls, *args, **kwargs):
        _instance = int.__new__(cls, *args, **kwargs)
        for attr in cls.STANDARD_ATTRS:
            setattr(_instance, attr, False)

        return _instance

    def __getattr__(self, attr):
        if attr == 'ago':
            _calc_factor = -1

        elif attr == 'after':
            _calc_factor = 1

        self._calc_date_x(_calc_factor)
        self._reset_attributes()
        return self._resultant_data

    def _reset_attributes(self):
        for attr in self.STANDARD_ATTRS:
            setattr(self, attr, False)
        return self

    @property
    def day(self):
        setattr(self, '_calc_day', True)
        return self

    @property
    def week(self):
        setattr(self, '_calc_week', True)
        return self

    @property
    def month(self):
        setattr(self, '_calc_month', True)
        return self

    def _calc_date_x(self, _calc_factor):
        if(getattr(self, '_calc_day')):
            _relative_delta = relativedelta(days=_calc_factor * self)

        elif(getattr(self, '_calc_week')):
            _relative_delta = relativedelta(weeks=_calc_factor * self)

        elif(getattr(self, '_calc_month')):
            _relative_delta = relativedelta(months=_calc_factor * self)

        else:
            raise Exception('Need days or weeks or months to compute datetime delta')

        _resultant_data = datetime.now() + _relative_delta
        setattr(self, '_resultant_data', _resultant_data)


def test_func():
    ex = ExtendedDateTime(1)

    try:
        print('Day Ago: ', ex.day.ago)
        print('Day After: ', ex.day.after)

        print('Week Ago: ', ex.week.ago)
        print('Week After: ', ex.week.after)

        print('Month Ago: ', ex.month.ago)
        print('Month After: ', ex.month.after)

        print('Error', ex.ago)

    except Exception as exp:
        print('Error: ', exp)
        sys.exit(-1)


if __name__ == '__main__':
    test_func()
