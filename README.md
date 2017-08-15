# datetimedelta
Calculates relative delta for Date time inline

```
from datetimedelta import ExtendedDateTime

# All calculations below are based on Date: 2017-08-16.  
extend_date_time_obj = ExtendedDateTime(2)

print(extend_date_time_obj.days.ago.date())      # 2017-08-14
print(extend_date_time_obj.days.after.date())    # 2017-08-18
print(extend_date_time_obj.weeks.ago.date())     # 2017-08-02
print(extend_date_time_obj.weeks.after.date())   # 2017-08-30
print(extend_date_time_obj.months.ago.date())    # 2017-06-16
print(extend_date_time_obj.months.after.date())  # 2017-10-16
print(extend_date_time_obj.years.ago.date())     # 2015-08-16
print(extend_date_time_obj.years.after.date())   # 2019-08-16

```
