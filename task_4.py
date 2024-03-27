import csv

stats = {}

with open('history_mirror.csv', mode='r', encoding='utf-8') as pin:
    reader = csv.reader(pin, delimiter=',')
    next(reader)
    for date, username, verdict in reader:
        year = date.split('-')[0]
        if year in stats:
            stats[year] += 1
        else:
            stats[year] = 1

for k, v in stats.items():
    print(f'В {k} году зеркало было использовано {v}.')
