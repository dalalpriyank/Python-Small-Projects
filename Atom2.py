# alphanums = string.ascii_letters + string.digits

import pdb  #break points pdb.set_trace()
import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

zoom_url = "https://api.zoom.us/v2/"
zoom_headers = {"authorization": "Bearer " + os.environ.get("ZOOM_TOKEN")}
user = "priyank@scbt.ca"

response = requests.post(zoom_url + "users/priyank@scbt.ca/meetings", headers = zoom_headers, json = {
    "topic": "Test meeting",
    "type": 2,
    "start_time": "2021-05-23T13:00:00",
    "duration": 120,
    "timezone": "America/New_York",
    "password": "stanford",
    "settings": {"host_video": True, "auto_recording": "cloud","use_pmi": True}
})
pdb.set_trace()


# def assign_meetings():
#
#     for user in requests.get(zoom_url + "users", params = {"page_size": 300}, headers = zoom_headers).json()["users"]:
#         users.add(user["email"])
#
#     date = datetime.date.today() + datetime.timedelta(days = int(request.values.get("day")))
#     for session in Sessions.query.join("session_datetimes").filter(Sessions.instructor_id != None, SessionDatetimes.date == date).options(
#         contains_eager("session_datetimes"),
#         subqueryload("instructor"),
#     ):
#         if session.instructor.email in users:
#             for session_datetime in session.session_datetimes:
#                 if session_datetime.meeting_token:
#                     boto3.client('sns').publish(TopicArn=os.environ.get("SNS_TOPIC_ARN"), Subject="Place Assigner Error", Message=str(session_datetime.id) + " is already assigned a meeting")
#                 else:
#                     response = requests.post(zoom_url + "users/" + session.instructor.email + "/meetings", headers = zoom_headers, json = {
#                         "topic": session.id,
#                         "type": 2,
#                         "start_time": datetime.datetime.combine(session_datetime.date, session_datetime.start_time).strftime("%Y-%m-%dT%H:%M:00"),
#                         "duration": (session_datetime.end_time.hour - session_datetime.start_time.hour) * 60 + session_datetime.end_time.minute - session_datetime.start_time.minute,
#                         "timezone": "America/New_York",
#                         "password": "".join([random.choice(alphanums) for i in range(10)]),
#                         "settings": {"host_video": True, "auto_recording": "cloud", "alternative_hosts": "gerald@scbt.ca"}
#                     })
#                     response = response.json()
#                     session_datetime.start_url = response["start_url"]
#                     session_datetime.join_url = response["join_url"]
#                     session_datetime.meeting_token = response["id"]
#         elif session.instructor.email != "cancelled@scbt.ca" and session.instructor.email != "tba@scbt.ca":
#             boto3.client('sns').publish(TopicArn=os.environ.get("SNS_TOPIC_ARN"), Subject="Place Assigner Error", Message=session.instructor.email + " cannot assign meeting")
#
#     db.session.commit()
#     return ("", 200)
