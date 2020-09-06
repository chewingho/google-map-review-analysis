from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re

def get_actual_date(move):
    today = datetime.today().strftime('%Y%m%d')
    if move.find(' 天前') != -1:
        regex = re.compile(r'(\d)( 天前)')
        substract = int(regex.search(move).group(1))
        relativedelta
        return (datetime.today() - relativedelta(days=substract)).strftime('%Y%m%d')
    elif move.find(' 週前') != -1:
        regex = re.compile(r'(\d)( 週前)')
        substract = int(regex.search(move).group(1))
        return (datetime.today() - relativedelta(weeks=substract)).strftime('%Y%m%d')
    elif move.find(' 個月前') != -1:
        regex = re.compile(r'(\d)( 個月前)')
        substract = int(regex.search(move).group(1))
        return (datetime.today() - relativedelta(months=substract)).strftime('%Y%m%d')
    elif move.find(' 年前') != -1:
        regex = re.compile(r'(\d)( 年前)') 
        substract = int(regex.search(move).group(1))
        return (datetime.today() - relativedelta(years=substract)).strftime('%Y%m%d')