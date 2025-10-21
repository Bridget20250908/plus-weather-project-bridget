from datetime import datetime


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date_object = datetime.fromisoformat(iso_string)
    date_string = date_object.strftime("%A %d %B %Y")

    return date_string


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celcisu = (float(temp_in_fahrenheit) - 32) * 5 / 9

    return round(temp_in_celcisu, 1)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C

# ---- Saturday 03 July 2021 ----
#   Minimum Temperature: 13.9°C
#   Maximum Temperature: 20.0°C

    count = 0
    return_string = {}
    date_list = []
    low_temp_list = []
    high_temp_list = []

    for i in weather_data:
        count += 1
        date = i[0]
        date_list.append(date)
        low_temp = i[1]
        low_temp_list.append(low_temp)
        high_temp = i[2]
        high_temp_list.append(high_temp)

        return_string += f"----{convert_date(date_list[i])}----\n"
        return_string += f" Minimum Temperature: {convert_f_to_c(low_temp_list[i])}\n"
        return_string += f" Maxmum Temperature: {convert_f_to_c(high_temp_list[i])}\n"
        return_string += f"\n"
        return return_string


weather_data = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

print(generate_daily_summary(weather_data))
