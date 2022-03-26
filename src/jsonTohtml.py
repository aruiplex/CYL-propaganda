import sys
from xml.etree import ElementTree as ET
import json


html = ET.Element('html')
body = ET.Element('body')
html.append(body)
table = ET.Element('table')
body.append(table)

data = json.load(open("choices_clean.json", encoding="utf-8"))

tr = ET.Element('tr')
table.append(tr)
for key in data["Mon"][0]:
    header = ET.Element('th')
    tr.append(header)
    header.text = key

for weekday in data:
    for video in data[weekday]:
        tr = ET.Element('tr')
        for attr in video:
            td = ET.Element('td')
            if attr == "pic":
                img = ET.Element('img')
                img.set("src", video[attr])
                img.set("style", "max-height:200px")
                td.append(img)
            else:
                td.text = str(video[attr])
            tr.append(td)
        table.append(tr)


ET.ElementTree(html).write(open("b.html", "w", encoding="utf-8"), encoding='unicode',
                           method='html')
