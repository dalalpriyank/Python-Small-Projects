import pdb  #break points pdb.set_trace()
import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

# pdb.set_trace()
zoom_url = "https://api.zoom.us/v2/"
zoom_headers = {"authorization": "Bearer " + os.environ.get("ZOOM_TOKEN")}

timeMondayToFridayMorning = ["2021-07-26T08:00:00","2021-07-27T08:00:00","2021-07-28T08:00:00","2021-07-29T08:00:00","2021-07-30T08:00:00"]
timeMondayToFridayEve     = ["2021-07-26T17:00:00","2021-07-27T17:00:00","2021-07-28T17:00:00","2021-07-29T17:00:00","2021-07-30T17:00:00"]
timeWeekend               = ["2021-07-31T09:00:00","2021-08-01T09:00:00"]
customTime                = ["2021-07-26T14:00:00","2021-07-27T14:00:00","2021-07-28T08:00:00","2021-07-29T08:00:00","2021-07-30T08:00:00"]

topic    = "G2 Weekend"
user     = "jameszfli@hotmail.com"
hours    = 6
for x in timeWeekend:
    response = requests.post(zoom_url + "users/"+user+"/meetings", headers = zoom_headers, json = {
        "topic": topic,
        "type": 2,
        "start_time": x,
        "duration": hours*60,
        "timezone": "America/New_York",
        "password": "stanford",
        "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
        })
