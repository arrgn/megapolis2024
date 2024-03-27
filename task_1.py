import csv

errors_list = []

with open('history_mirror.csv', mode='r', encoding='utf-8') as pin:
    reader = csv.reader(pin, delimiter=',')
    fieldnames = next(reader)
    for date, username, verdict in reader:
        if 'Победа над смертью' in verdict:
            errors_list.append((date, username))

with open('mirror_error.csv', mode='w', encoding='utf-8') as pout:
    writer = csv.writer(pout, delimiter=',')
    writer.writerow(fieldnames[:-1])
    writer.writerows(errors_list)

date, username = sorted(errors_list)[0]
name = username.split()[0] + ' '
name += ''.join(map(lambda x: x[0] + '.', username.split()[1:]))
print(f'Сообщение было зафиксировано: {date} у пользователя {name}')
