import requests

"""test pic download and save
"""

res = requests.get(
    "http://i0.hdslb.com/bfs/archive/a89cc9e30776d72a673801e411c90855560fb55d.jpg")
with open("test.jpg", "wb") as f:
    f.write(res.content)
