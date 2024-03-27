import csv

command = input()

while command != 'stop':
    first_name, second_name = command.split()

    with open('history_mirror.csv', mode='r', encoding='utf-8') as pin:
        reader = csv.reader(pin, delimiter=',')
        found = False
        for date, username, verdict in reader:
            if first_name in username and second_name in username:
                found = True
                name_split = username.split()
                name = name_split[0] + ' '
                name += ''.join(map(lambda x: x[0] + '.', name_split[1:]))
                print(f'Предсказание для {name} - {verdict}')
        if not found:
            print('Вас не нашлось в записях')

    command = input()
