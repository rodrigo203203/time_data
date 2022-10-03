import datetime 

DATE_FORMAT = "%m/%d/%Y"

def get_default_date_data(start_date, end_date, default_value):
    if start_date is None or end_date is None:
        return None
    elif start_date > end_date:
        return None
    begin_date = datetime.datetime.strptime(start_date,DATE_FORMAT)
    end_date = datetime.datetime.strptime(end_date,DATE_FORMAT)
    total_days = (end_date - begin_date).days +1
    dates =[]
    for single_day in range(total_days):
        current_date = (begin_date + datetime.timedelta(days = single_day)).date()
        string_date = current_date.strftime(DATE_FORMAT)
        dates.append({'date': string_date,'participants':default_value})
    return dates