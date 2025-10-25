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
        list = []
        for row in reader:
            if row:
                list.append([row[0], int(row[1]), int(row[2])])
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
    if not weather_data:
        return ()
    result_string = ""
    day_count = len(weather_data)
    low_temp_list = []
    high_temp_list = []
    date_list = []

    for i in weather_data:
        low_temp = i[1]
        low_temp_list.append(low_temp)
        high_temp = i[2]
        high_temp_list.append(high_temp)
        date = i[0]
        date_list.append(date)

    lowest_temp = min(low_temp_list)
    lowest_temp_string = format_temperature(convert_f_to_c(lowest_temp))
    lowest_temp_index = low_temp_list.index(lowest_temp)
    lowest_temp_date = convert_date(date_list[lowest_temp_index])
    average_low_temp = calculate_mean(low_temp_list)
    average_low_temp_string = format_temperature(
        convert_f_to_c(average_low_temp))
    highest_temp = max(high_temp_list)
    highest_temp_string = format_temperature(convert_f_to_c(highest_temp))
    highest_temp_index = high_temp_list.index(highest_temp)
    highest_temp_date = convert_date(date_list[highest_temp_index])
    average_high_temp = calculate_mean(high_temp_list)
    average_high_temp_string = format_temperature(
        convert_f_to_c(average_high_temp))

    result_string += f"{day_count} Day Overview\n"
    result_string += f"  The lowest temperature will be {lowest_temp_string}, and will occur on {lowest_temp_date}.\n"
    result_string += f"  The highest temperature will be {highest_temp_string}, and will occur on {highest_temp_date}.\n"
    result_string += f"  The average low this week is {average_low_temp_string}.\n"
    result_string += f"  The average high this week is {average_high_temp_string}.\n"
    return result_string
    # print(f"5 Day Overview")
    # print(
    #     "The lowest temperature will be {lowest_temp} {DEGREE_SYMBOL},and will occur on {lowest_temp_date}")
    # print(
    #     "The highest temperature will be {hightest_temp}{DEGREE_SYMBOL}, and will occur on {highest_temp_date}")
    # print("The average low his week is {average_low_temp}")
    # print("The average high this week is {average_high_temp} ")
    # test = " 5 day Summar \n"
    # print(f"test")


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

    if not weather_data:
        return ()
    count = 0
    return_string = ""
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

        return_string += f"---- {convert_date(date)} ----\n"
        return_string += f"  Minimum Temperature: {format_temperature(convert_f_to_c(low_temp))}\n"
        return_string += f"  Maximum Temperature: {format_temperature(convert_f_to_c(high_temp))}\n"
        return_string += f"\n"
    return return_string
