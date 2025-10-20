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
    low_temp_list = []
    high_temp_list = []

    for i in weather_data:
        low_temp = i[1]
        low_temp_list.append(low_temp)
        high_temp = i[2]
        high_temp_list.append(high_temp)
    lowest_temp = min(low_temp_list)
    lowest_temp_index = low_temp_list.index(lowest_temp)
    average_low_temp = calculate_mean(low_temp_list)
    highest_temp = max(high_temp_list)
    highest_temp_index = high_temp_list.index(highest_temp)
    average_high_temp = calculate_mean(high_temp_list)
    print(
        f"5 Day Overview\n The lowest temperatur will be {lowest_temp}, and will occur on {lowest_temp_index}.")


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


    #     min_index = weather_data.index(lowest_temp)
    #     lowest_date = weather_data[min_index[0]]
    # return (lowest_date, lowest_temp)
weather_data = [["2020-06-19T07:00:00+08:00", -7, 10],
                ["2020-06-20T07:00:00+08:00", -51, 67],
                ["2020-06-21T07:00:00+08:00", 58, 72],
                ["2020-06-22T07:00:00+08:00", 59, 71],
                ["2020-06-23T07:00:00+08:00", -52, 71],
                ["2020-06-24T07:00:00+08:00", 52, 67],
                ["2020-06-25T07:00:00+08:00", -48, 66],
                ["2020-06-26T07:00:00+08:00", 53, 66]]
print(generate_summary(weather_data))
