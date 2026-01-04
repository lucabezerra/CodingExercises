from datetime import datetime, timedelta

WEEKDAYS_LIST = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def format_date(dt):
    return datetime.strftime(dt, "%Y-%m-%dT%H:%M:%S")

def get_first_workday(dt):
    dt = dt.replace(day=1)
    day = datetime.strftime(dt, "%A")
    while day not in WEEKDAYS_LIST:
        dt += timedelta(days=1)
        day = datetime.strftime(dt, "%A")
    return dt

def get_last_workday(dt):
    day = datetime.strftime(dt, "%A")
    while day not in WEEKDAYS_LIST:
        dt += timedelta(days=-1)
        day = datetime.strftime(dt, "%A")
    return dt

def get_quarter_by_month(month_num):
     match month_num:
        case 1 | 2 | 3:
            return 1
        case 4 | 5 | 6:
            return 2
        case 7 | 8 | 9:
            return 3
        case 10 | 11 | 12:
            return 4
        case _:
            raise Exception("What month is this?!")

def get_quarter_last_day(quarter_num):
    match quarter_num:
        case 1:
            return "03-31"
        case 2:
            return "06-30"
        case 3:
            return "09-30"
        case 4:
            return "12-31"
        case _:
            raise Exception("What quarter is this?!")

def delivery_date(start, description):
    start_dt = datetime.fromisoformat(start)
    if description in ["NOW", "ASAP", "EOW"]:
        if description == "NOW":
            return format_date(start_dt + timedelta(hours=2))
        elif description == "ASAP":
            if start_dt.hour < 13:
                return format_date(start_dt.replace(hour=17, minute=0))
            else:
                tomorrow = (start_dt + timedelta(days=1))
                return format_date(tomorrow.replace(hour=13, minute=0))
        elif description == "EOW":
            day = datetime.strftime(start_dt, "%A")
            for i, weekday in enumerate(WEEKDAYS_LIST):
                if day == weekday:
                    if i <= 2:
                        return_date = (start_dt + timedelta(days=(4-i))).replace(hour=17, minute=0)
                    else:
                        return_date = (start_dt + timedelta(days=(6-i))).replace(hour=20, minute=0)
            return format_date(return_date)
    else:
        if description[-1] == "M":
            month_num = int(description[:-1])
            return_date = None
            if start_dt.month < month_num:
                return_date = start_dt.replace(month=month_num, hour=8, minute=0)
            else:
                return_date = start_dt.replace(year=start_dt.year + 1, month=month_num, hour=8, minute=0)

            return_date = get_first_workday(return_date)
            return format_date(return_date)
        elif description[0] == "Q":
            quarter_num = int(description[1:])
            return_date = None

            start_quarter = get_quarter_by_month(start_dt.month)
            quarter_last_day = get_quarter_last_day(quarter_num)

            if start_quarter <= quarter_num:
                return_date = datetime.fromisoformat(f"{start_dt.year}-{quarter_last_day}T08:00:00")
            else:
                return_date = datetime.fromisoformat(f"{start_dt.year+1}-{quarter_last_day}T08:00:00")

            return_date = get_last_workday(return_date)
            return format_date(return_date)