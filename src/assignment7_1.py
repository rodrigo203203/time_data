import datetime

DATE_FORMAT = "%m/%d/%Y"

def get_dates_in_interval(start,end):
    if start is None or end is None:
        return None
    elif start > end:
        return None
    begin_date = datetime.datetime.strptime(start,DATE_FORMAT)
    end_date = datetime.datetime.strptime(end,DATE_FORMAT)
    total_days = (end_date - begin_date).days +1
    date = []
    for single_day in range(total_days):
        current_date = (begin_date + datetime.timedelta(days = single_day)).date()
        string_date = current_date.strftime(DATE_FORMAT)
        date.append(string_date)
    return date