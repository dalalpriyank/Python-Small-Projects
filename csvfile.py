import csv
import pdb
import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

zoom_url = "https://api.zoom.us/v2/"
zoom_headers = {"authorization": "Bearer " + os.environ.get("ZOOM_TOKEN")}
numeOfRow = 1

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        response = requests.post(zoom_url + "users/"+row[0].strip()+"/meetings", headers = zoom_headers, json = {
            "topic": row[3],
            "type": 2,
            "start_time": row[1],
            "duration": int(row[2])*60,
            "timezone": "America/New_York",
            "password": "stanford",
            "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
        })
        #pdb.set_trace()
        print(numeOfRow, ")",row[0]," status is ", response.status_code," on",row[1])
        f = open("demofile2.txt", "a")
        f.write(str(numeOfRow)+" )"+row[0]+"status is  "+str(response.status_code)+" on "+row[1]+" \n")
        f.close()
        numeOfRow += 1
