from datetime import datetime, timedelta


def convert_cmc_date_str_to_yyyymmdd(cmc_date_str):
    # date_time_str = "Jan 29, 2018"
    date_object = datetime.strptime(cmc_date_str, '%b %d, %Y')
    yyyymmdd = int(date_object.strftime('%Y%m%d'))
    return yyyymmdd


def subtract_days_from_date(yyyymmdd, days):
    # Convert the input to a datetime object
    if isinstance(yyyymmdd, str):
        date = datetime.strptime(yyyymmdd, '%Y%m%d')
    elif isinstance(yyyymmdd, int):
        date = datetime.strptime(str(yyyymmdd), '%Y%m%d')
    else:
        raise ValueError("Invalid date format")

    # Subtract the specified number of days from the date
    result_date = date - timedelta(days=days)

    # Return the resulting date in the format "YYYYMMDD"
    return int(result_date.strftime('%Y%m%d'))


def get_date_text_values(yyyymmdd):
    # Import the datetime module

    if isinstance(yyyymmdd, str):
        # Convert the input to a datetime object
        date = datetime.strptime(yyyymmdd, '%Y%m%d')
    elif isinstance(yyyymmdd, int):
        # Convert the input to a string and then to a datetime object
        date = datetime.strptime(str(yyyymmdd), '%Y%m%d')
    else:
        raise ValueError("Invalid date format")

    # Get the year, month, and date as separate values
    year_text_value = str(date.year)
    month_text_value = date.strftime("%b")  # "Feb" for February, etc.
    date_text_value = str(date.day).zfill(2)  # "20" instead of "20"

    return year_text_value, month_text_value, date_text_value


def current_time_formatted_str():
    now = datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M")
