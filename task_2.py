import csv

with open('history_mirror.csv', mode='r', encoding='utf-8') as pin:
    reader = csv.reader(pin, delimiter=',')
    data = list(reader)

for i in range(len(data), 0, -1):
    for j in range(1, i):
        if data[j - 1][2] > data[j][2]:
            temp = data[j]
            data[j] = data[j - 1]
            data[j - 1] = temp

for row in data[:4]:
    print(' - '.join(row))
