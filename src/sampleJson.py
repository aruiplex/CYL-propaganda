import json
import random

data = json.load(open('data.json', 'r', encoding='utf-8'))
choices = {'Mon': [], 'Tue': [], 'Wed': [],
           'Thu': [], 'Fri': [], 'Sat': [], 'Sun': []}

num = 0
while True:
    d = random.randint(0, len(data)-1)
    weekday = data[d]['weekday']
    if len(choices[weekday]) < 10 and data[d]["created_date"][:4] not in ["2022", "2016"]:
        choices[weekday].append(data[d])
        num += 1
    if num == 70:
        break

json.dump(choices, open('choices.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=4)
