#!/usr/bin/python3
# This module gives extended functionality for calculating datetime based on
# functionality that exists in Ruby
from datetime import datetime
import sys

class ExtendedDateTime(int):
    def __new__(cls, *args, **kwargs):
        _instance = int.__new__(cls, *args, **kwargs)
        setattr(_instance, 'current_date', datetime.now())
        return _instance

    def __getattr__(self, attr):
        if attr == 'ago':
            print('ATTR: ', attr)

        else:
            return

    @property
    def day(self):
        return self

    @property
    def week(self):
        return self

    @property
    def month(self):
        return self


def main():
    ex = ExtendedDateTime(12)
    print('Value: ', ex)

    print('Day: ', ex.day)
    print('Week: ', ex.week)
    print('Month: ', ex.month)

    try:
        print('Chained: ', ex.day.week.month.ago)

    except Exception as exp:
        print(exp)
        sys.exit(-1)


if __name__ == '__main__':
    main()
