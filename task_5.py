import csv

codes = {}

for i in range(ord('А'), ord('я') + 1):
    codes[chr(i)] = i - ord('А') + 1
codes['ё'] = 65
codes['Ё'] = 66
codes[' '] = 67

with open('users_with_hash.csv', mode='w', encoding='utf-8') as pout:
    writer = csv.writer(pout, delimiter=',')
    writer.writerow('ID,date,username,verdict'.split(','))
    with open('history_mirror.csv', mode='r', encoding='utf-8') as pin:
        reader = csv.reader(pin, delimiter=',')
        next(reader)
        for date, username, verdict in reader:
            p = 67
            m = 10 ** 9 + 9
            hash_ = 0
            for i in range(len(username)):
                hash_ += codes[username[i]] * p ** i % m
            writer.writerow((hash_, date, username, verdict))
