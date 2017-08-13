#!/usr/bin/python3
# This module gives extended functionality for calculating datetime based on
# functionality that exists in Ruby
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ExtendedDateTime(int):
    _DELTA_ATTRS = ['_calc_days', '_calc_weeks', '_calc_months', '_calc_years']

    def __new__(cls, *args, **kwargs):
        _instance = int.__new__(cls, *args, **kwargs)
        for attr in cls._DELTA_ATTRS:
            setattr(_instance, attr, False)

        return _instance

    def __getattr__(self, attr):
        if attr == 'ago':
            _calc_factor = -1

        elif attr == 'after':
            _calc_factor = 1

        self._calc_date_x(_calc_factor)
        self._reset_attributes()
        return self._resultant_date

    def _reset_attributes(self):
        for attr in self._DELTA_ATTRS:
            setattr(self, attr, False)
        return self

    @property
    def days(self):
        setattr(self, '_calc_days', True)
        return self

    @property
    def weeks(self):
        setattr(self, '_calc_weeks', True)
        return self

    @property
    def months(self):
        setattr(self, '_calc_months', True)
        return self

    @property
    def years(self):
        setattr(self, '_calc_years', True)
        return self

    def _calc_date_x(self, _calc_factor):
        if(getattr(self, '_calc_days')):
            _relative_delta = relativedelta(days=_calc_factor * self)

        elif(getattr(self, '_calc_weeks')):
            _relative_delta = relativedelta(weeks=_calc_factor * self)

        elif(getattr(self, '_calc_months')):
            _relative_delta = relativedelta(months=_calc_factor * self)

        elif(getattr(self, '_calc_years')):
            _relative_delta = relativedelta(years=_calc_factor * self)

        else:
            raise Exception('Need days or weeks or months or years to compute datetime delta')

        _resultant_date = datetime.now() + _relative_delta
        setattr(self, '_resultant_date', _resultant_date)
