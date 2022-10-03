import datetime 

DATE_FORMAT = "%m/%d/%Y"

def special_case(start, end , default):
    begin_date = datetime.datetime.strptime(start,DATE_FORMAT)
    end_date = datetime.datetime.strptime(end,DATE_FORMAT)
    total_days = (end_date - begin_date).days +1
    dates =[]
    for single_day in range(total_days):
        current_date = (begin_date + datetime.timedelta(days = single_day)).date()
        string_date = current_date.strftime(DATE_FORMAT)
        dates.append({'date': string_date,'participants':default})
    return dates   

def get_default_date_data(start_date, end_date, default_value):
    if start_date is None or end_date is None:
        start = '9/12/2022'
        end = '9/15/2022'
        extra_case = special_case(start, end, default_value)
        return extra_case 
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

   