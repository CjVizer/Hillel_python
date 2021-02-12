"""
Дан текстовый файл со статистикой посещения сайта за неделю.
Каждая строка содержит ip адрес, время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
Для каждого ip укажите количество посещений, наиболее популярный день недели.
Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
"""

from datetime import timedelta

db = {}
timeline = []


def most_visited_day(list_of_days):
    result = ''
    for value in list_of_days:
        if list_of_days.count(value) > list_of_days.count(result):
            result = value
    return result


with open('statistic.txt', 'r', encoding='utf-8') as statistic:
    for line in statistic:
        ip, time, weekday = line.strip('\n').split()
        if not db.get(ip, 0):
            db[ip] = {'total_visits': 1,
                      'visit_days': [weekday]}
        else:
            db[ip]['total_visits'] += 1
            db[ip]['visit_days'].append(weekday)
        time_seconds = list(map(int, time.split(':')))
        timeline.append(time_seconds[0] * 3600 + time_seconds[1] * 60 + time_seconds[2])
    timeline.sort()

time_range = []
timeline_length = len(timeline)
for idx in range(timeline_length - 1):
    time_range_temp = [timeline[idx]]
    for idx_temp in range(idx + 1, timeline_length):
        if timeline[idx_temp] - time_range_temp[0] < 3600:
            time_range_temp.append(timeline[idx_temp])
        else:
            if len(time_range) < len(time_range_temp):
                time_range = time_range_temp
            break

with open('statistic_modified.txt', 'w', encoding='utf-8') as statistic_modified:
    for item in db:
        statistic_modified.write(f"IP: {item:>15}  "
                                 f"Total visits: {db[item]['total_visits']:>2}  "
                                 f"Most visited day: {most_visited_day(db[item]['visit_days'])}\n")
    statistic_modified.write(f'Most visited time: '
                             f'{str(timedelta(seconds=time_range[0]))} - {str(timedelta(seconds=time_range[-1]))}')
