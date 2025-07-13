from datetime import datetime, timedelta

def time_ago(seconds):
    return str(timedelta(seconds=seconds))

def current_time(fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(fmt)

def days_between(d1, d2, fmt="%Y-%m-%d"):
    d1 = datetime.strptime(d1, fmt)
    d2 = datetime.strptime(d2, fmt)
    return abs((d2 - d1).days)
