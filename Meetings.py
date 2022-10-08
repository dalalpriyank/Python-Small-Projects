import pdb  #break points pdb.set_trace()
import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

zoom_url = "https://api.zoom.us/v2/"
zoom_headers = {"authorization": "Bearer " + os.environ.get("ZOOM_TOKEN")}

user = "priyank@scbt.ca"
topic = "Elect Code"
duration = 60*6
timea1 = "2021-05-29T09:00:00"
timea2 = "2021-05-26T15:00:00"
timea3 = "2021-05-27T15:00:00"
timea1 = "2021-05-28T15:00:00"

response = requests.post(zoom_url + "users/"+user+"/meetings", headers = zoom_headers, json = {
    "topic": topic,
    "type": 2,
    "start_time": timea1,
    "duration": duration,
    "timezone": "America/New_York",
    "password": "stanford",
    "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
})
response = requests.post(zoom_url + "users/"+user+"/meetings", headers = zoom_headers, json = {
    "topic": topic,
    "type": 2,
    "start_time": timea2,
    "duration": duration,
    "timezone": "America/New_York",
    "password": "stanford",
    "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
})
response = requests.post(zoom_url + "users/"+user+"/meetings", headers = zoom_headers, json = {
    "topic": topic,
    "type": 2,
    "start_time": timea3,
    "duration": duration,
    "timezone": "America/New_York",
    "password": "stanford",
    "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
})
    # response = requests.post(zoom_url + "users/"+user+"/meetings", headers = zoom_headers, json = {
    #     "topic": topic,
    #     "type": 2,
    #     "start_time": timea4,
    #     "duration": duration,
    #     "timezone": "America/New_York",
    #     "password": "stanford",
    #     "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
    # })

#pdb.set_trace()
