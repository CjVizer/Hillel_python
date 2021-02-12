"""
Дан текстовый файл со статистикой посещения сайта за неделю.
Каждая строка содержит ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
Для каждого ip укажите количество посещений, наиболее популярный день недели.
Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
"""

from datetime import timedelta

db = {}  # Database. Format example: {'192.168.0.1': {'total_visits': 0, visit_days: [sunday, monday]}}
timeline = []  # Time keeping list


def most_visited_day(list_of_days):
    """Function for calculating the most popular visit day for an ip address"""
    result = ''
    for value in list_of_days:
        if list_of_days.count(value) > list_of_days.count(result):
            result = value
    return result


# In this part of the code, we create a structured database for our needs.
with open('statistic.txt', 'r', encoding='utf-8') as statistic:
    for line in statistic:  # Reading data from a file line by line then we cut off the line break,
        ip, time, weekday = line.strip('\n').split()  # split the line with spaces, and write the values to variables.
        if not db.get(ip):  # If key[ip] is not in the database
            db[ip] = {'total_visits': 1, 'visit_days': [weekday]}  # initialize key - value
        else:  # else increase "total_visit" by 1 and add the day of the week to the visit_day list
            db[ip]['total_visits'] += 1
            db[ip]['visit_days'].append(weekday)
            # Convert time to seconds and add the result to the "timeline" list
        time_to_seconds = list(map(int, time.split(':')))  # Variable for storing values "hours", "minutes", "seconds"
        timeline.append(time_to_seconds[0] * 3600 + time_to_seconds[1] * 60 + time_to_seconds[2])
    timeline.sort()  # Then we sort the list

# In this part of the code, we calculate the most popular visit time in the range of one hour
time_range = []
timeline_length = len(timeline)
for idx in range(timeline_length - 1):  # We take a value from the list
    time_range_temp = [timeline[idx]]  # We immediately write this value into a new temporary list
    for idx_temp in range(idx + 1, timeline_length):
        # Then, values that fall within the range of one hour from the first value in the temporary list,
        # we add to the same list
        if timeline[idx_temp] - time_range_temp[0] < 3600:
            time_range_temp.append(timeline[idx_temp])
        else:
            # Then we check if the length of the "time_range" list is less than the length of the temporary list,
            # we overwrite the list "time_range" with values from the temporary list.
            if len(time_range) < len(time_range_temp):
                time_range = time_range_temp
            break
            # Thus, we get the list with the largest number of visits in the range of one hour.
            # All values in the list "time_range" are seconds.

# In this part of the code, we format the lines and write them to a new file
with open('statistic_modified.txt', 'w', encoding='utf-8') as statistic_modified:
    for item in db:
        statistic_modified.write(f"IP: {item:>15}  "
                                 f"Total visits: {db[item]['total_visits']:>2}  "
                                 f"Most visited day: {most_visited_day(db[item]['visit_days'])}\n")
    statistic_modified.write(f'Most visited time: '
                             f'{str(timedelta(seconds=time_range[0]))} - {str(timedelta(seconds=time_range[-1]))}')
