"""
Дан текстовый файл со статистикой посещения сайта за неделю.
Каждая строка содержит ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
Для каждого ip укажите количество посещений, наиболее популярный день недели.
Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
"""


def most_visited_day(list_of_days):
    """
    Function for calculating the most popular visit day for an ip address
    :param list_of_days: List of days (type: list ['monday', 'tuesday',...])
    :return: The element that appears most often in the list (type: str)
    """
    result = ''
    for value in list_of_days:
        if list_of_days.count(value) > list_of_days.count(result):
            result = value
    return result


def time_to_seconds(time_value):
    """
    Function for converting time to seconds
    :param time_value: time (type: str '12:22:03')
    :return: seconds (type: int)
    """
    seconds = list(map(int, time_value.split(':')))  # Variable for storing values "hours", "minutes", "seconds"
    return seconds[0] * 3600 + seconds[1] * 60 + seconds[2]


def seconds_to_time(seconds_value):
    """
    Function for converting seconds to time
    :param seconds_value: seconds (type: int)
    :return: time (type: str '12:22:03')
    """
    hours = seconds_value // 3600
    minutes = (seconds_value - hours * 3600) // 60
    seconds = seconds_value - hours * 3600 - minutes * 60
    return f'{hours:>02}:{minutes:>02}:{seconds:>02}'


def rush_hour(timeline_list):
    """Function for calculating the most popular visit time in the range of one hour"""
    time_range = []
    timeline_length = len(timeline_list)
    for idx in range(timeline_length - 1):  # We take a value from the list
        time_range_temp = [timeline_list[idx]]  # We immediately write this value into a new temporary list
        for idx_temp in range(idx + 1, timeline_length):
            # Then, values that fall within the range of one hour from the first value in the temporary list,
            # we add to the same list
            if timeline_list[idx_temp] - time_range_temp[0] < 3600:
                time_range_temp.append(timeline_list[idx_temp])
            else:
                # Then we check if the length of the "time_range" list is less than the length of the temporary list,
                # we overwrite the list "time_range" with values from the temporary list.
                if len(time_range) < len(time_range_temp):
                    time_range = time_range_temp
                break
                # Thus, we get the list with the largest number of visits in the range of one hour.
                # All values in the list "time_range" are seconds.
    return f'{seconds_to_time(time_range[0])} - {seconds_to_time(time_range[-1])}'


def get_statistic(in_file, out_file):
    """
    This function creates statistics for each ip address, and also calculates rush hour
    :param in_file: Name of input text file (format for each line: '139.18.150.126 23:12:44 sunday\n')
    :param out_file: Name of output file (format example: 'IP: 194.4.26.172  Total visits:  6  Most visited day: sunday)
    :return: None
    """
    db = {}  # Database. Format example: {'192.168.0.1': {'total_visits': 0, visit_days: [sunday, monday]}}
    timeline = []  # Time keeping list
    # In this part of the code, we create a structured database for our needs.
    try:
        with open(in_file, 'r', encoding='utf-8') as input_file:
            for line in input_file:  # Reading data from a file line by line then we cut off the line break,
                ip, time, weekday = line.strip('\n').split()  # split the line with spaces, and write to variables.
                if not db.get(ip, ''):  # If key[ip] is not in the database
                    db[ip] = {'total_visits': 1, 'visit_days': [weekday]}  # initialize key - value
                else:  # else increase "total_visit" by 1 and add the day of the week to the visit_day list
                    db[ip]['total_visits'] += 1
                    db[ip]['visit_days'].append(weekday)
                timeline.append(time_to_seconds(time))  # Convert time to seconds and add the result to the list
            timeline.sort()  # Then we sort the list
    except FileNotFoundError:
        print(f'File with the name "{in_file}" does not exist')

    # In this part of the code, we format the lines and write them to a new file
    with open(out_file, 'w', encoding='utf-8') as output_file:
        for item in db:
            output_file.write(f"IP: {item:>15}  "
                              f"Total visits: {db[item]['total_visits']:>2}  "
                              f"Most visited day: {most_visited_day(db[item]['visit_days'])}\n")
        output_file.write(f'Most visited time: {rush_hour(timeline)}')


get_statistic('statistic.txt', 'statistic_modified.txt')
