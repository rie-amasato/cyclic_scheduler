from flask import Flask


import schedule
import requests

import time
import datetime
import os

def DCsend(message,name):
	print(name,": " , os.environ[name])
	discordWH=os.environ[name]
	data={"content":" "+str(message)+" "}
	requests.post(discordWH,data=data)
  
def job():
    print("JOB", datetime.datetime.now())
    DCsend("Job"+str(datetime.datetime.now()), "WHURL")


schedule.every().minute.at(":00").do(job)

app=Flask(__name__)
@app.route("/")
def index():
  print("JOB", datetime.datetime.now())
  DCsend("Job"+str(datetime.datetime.now()), "WHURL")
  return "Job"+str(datetime.datetime.now())


