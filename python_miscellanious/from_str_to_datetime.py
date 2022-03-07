from datetime import datetime


s1 = '2015-01-19 13:26:00, 2015-01-19 13:30:35'


def make_datetime_obj(s):
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')


def get_delta_from_datetime(s):
    date_time_0, date_time_1 = s.split(', ')
    date_time_obj_0 = make_datetime_obj(date_time_0)
    date_time_obj_1 = make_datetime_obj(date_time_1)
    return date_time_obj_1 - date_time_obj_0


delta_obj = get_delta_from_datetime(s1)
print(delta_obj)
delta_in_sec = delta_obj.total_seconds()
print(delta_in_sec)
