import json

data = json.load(open("dev/choices.json", encoding="utf-8"))

for weekday in data:
    for video in data[weekday]:
        for attr in list(video.keys()):
            if attr not in ["pic", "title", "comment", "play", "description", "title", "length", "created_date", "weekday"]:
                video.pop(attr)

json.dump(data, open("choices_clean.json", "w", encoding="utf-8"),
          indent=4, ensure_ascii=False)
