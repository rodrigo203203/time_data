from datetime import date
from src.assignment7_1 import get_dates_in_interval
from src.assignnment7_2 import get_default_date_data
import unittest


def test_one_date():
    start_date = '09/12/2022'
    end_date = '09/12/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert '09/12/2022' in dates

def test_in_two_dates():
    start_date = '9/12/2022'
    end_date = '9/15/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert '09/12/2022' in dates
    assert '09/13/2022' in dates
    assert '09/14/2022' in dates
    assert '09/15/2022' in dates

def test_start_bigger_than_end():
    start_date = '9/15/2022'
    end_date = '9/10/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None

def test_two_dates_is_none():
    start_date = None
    end_date = None

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None 

    # Assignments 7.2
def test_equals_are_value_negative_number():
    start_date = '09/12/2022'
    end_date = '09/12/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date':'09/12/2022', 'participants':-99999} in dates

def test_date_default_value_none():
    start_date = '09/12/2022'
    end_date = '09/15/2022'
    default_value = None

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '09/12/2022', 'participants': None} in dates
    assert {'date': '09/13/2022', 'participants': None} in dates
    assert {'date': '09/14/2022', 'participants': None} in dates
    assert {'date': '09/15/2022', 'participants': None} in dates


def test_none_defaut_value_zerohours():
    start_date = None
    end_date = None
    default_value = '0h 0m'

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '09/12/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/13/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/14/2022', 'participants': '0h 0m'} in dates
    assert {'date': '09/15/2022', 'participants': '0h 0m'} in dates


def test_default_value_negative_nine():
    start_date = '09/12/2022'
    end_date = '09/15/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '09/12/2022', 'participants': -99999} in dates
    assert {'date': '09/13/2022', 'participants': -99999} in dates
    assert {'date': '09/14/2022', 'participants': -99999} in dates
    assert {'date': '09/15/2022', 'participants': -99999} in dates
        
        