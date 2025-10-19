import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
#   with open(".tests/data/example.csv") as file:
#       reader = csv.reader(file)
#       next(reader)
#       for row in reader:
#           temp_min = row[1]
#           temp_max = row[2]
    return f"{temp}{DEGREE_SYMBOL}"


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


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data_sum = 0
    for i in weather_data:
        weather_data_sum = weather_data_sum+float(i)
    if len(weather_data) != 0:
        mean = weather_data_sum / len(weather_data)
        return mean
    else:
        return f"No Weather Data Found"


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
    for row in reader:
        count = count+1
        return count
    for i in count:
        list[i] = row[i]
        return list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    #  last_index = max(i for i, x in enumerate(my_list) if x == search_value)
    if not weather_data:
        return ()
    for i in weather_data:

        min_value = min(weather_data)
        min_last_index = max(i for i, x in enumerate(
            weather_data) if x == min_value)
        # min_index = weather_data.index(min_value)
    return (float(min_value), min_last_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    for i in weather_data:

        max_value = max(weather_data)
        # max_index = weather_data.index(max_value)
        max_last_index = max(i for i, x in enumerate(
            weather_data) if x == max_value)
    return (float(max_value), max_last_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information:

        5 Day Overview
    The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    The average low this week is 12.2°C.
    The average high this week is 17.8°C.
    """
    for i in weather_data:
        lowest_temp = min(weather_data)
        min_index = weather_data.index(lowest_temp)
        lowest_date = convert_date(weather_data[min_index[0]])

        highest_temp = max(weather_data)

        lowest_temp_date = weather_data.index(lowest_temp)

        highest_temp_date = weather_data.index(highest_temp)

        average_low = calculate_mean(weather_data)
        average_high = calculate_mean(weather_data)

        multi_string = """
"""

        return (f"5 Day Overview\n The lowest temperatur will be {lowest_temp}, {DEGREE_SYMBOL}, and will occur on {lowest_temp_date}.\n The highest temperature will be {highest_temp}, {DEGREE_SYMBOL}, and will occur on {highest_temp_date}.\n The average low this week is {average_low}, {DEGREE_SYMBOL}.\n The average high this week is {average_high}, {DEGREE_SYMBOL}\n")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


pass
