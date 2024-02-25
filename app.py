from flask import Flask

import threading

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


def thread():
	minute_wait=1
	DCsend(str(minute_wait)+"分スレッドの開始", "WHURL")
	for t in range (minute_wait*12):
		time.sleep(10)
		DCsend(str(t)+" Threading...", "WHURL")
	DCsend(str(minute_wait)+"スレッド完了", "WHURL")

@app.route("/test_threading")
def test_threading():
	t1=threading.Thread(target=thread)
	t1.start()
	time.sleep(25)
	DCsend("スレッド外", "WHURL")
	return "test_threading"
