import time
import logging
import requests
import json
import pickle

logout = logging.getLogger(__name__+".stdout_logger")
logout.setLevel(logging.INFO)
logout.addHandler(logging.StreamHandler())

logfile = logging.getLogger(__name__+".file_logger")
logfile.setLevel(logging.INFO)
fh = logging.FileHandler("log.txt")
fh.setLevel(logging.INFO)
logfile.addHandler(fh)

s = requests.Session()
video_ctr = 0

f = []


def pa(pn):
    try:
        base_url = f"https://api.bilibili.com/x/space/arc/search?mid=20165629&ps=30&tid=0&pn={pn}&keyword=&order=pubdate&jsonp=jsonp"
        response = s.get(base_url)
        response.encoding = 'utf-8'
        j = json.loads(response.text)

        # video list
        vlist = j["data"]["list"]["vlist"]

        # if video list is empty
        if len(vlist) == 0:
            return

        # video in list
        for video in vlist:
            created = video["created"]
            # add attrs to video
            # create date
            video["created_date"] = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.gmtime(created))
            # weekday name: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            video["weekday"] = time.strftime("%a", time.gmtime(created))

        logout.info(f"{pn} done")
        time.sleep(0.5)

    except Exception as e:
        logfile.error(e)
        logout.error(e)


if __name__ == "__main__":
    # 123page in total
    vs = [x for x in range(123)]
    for v in vs:
        pa(v)

    # persist
    pickle.dump(f, open("vlist.pkl", "wb"))
    json.dump(f, open("data.json", "w", encoding="utf-8"), ensure_ascii=False)
