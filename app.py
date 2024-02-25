from flask import Flask

import threading

import schedule
import requests

import time
import datetime
import os


app=Flask(__name__)

def th_keepliving(sec):
	for i in range(int(sec/10)+1):
		print("th_keepliving", i)
		print((os.getenv("CYCLIC_URL")+"/keepliving"))
		print(requests.get(os.getenv("CYCLIC_URL")+"/keepliving"))
		time.sleep(20)
		print("next...")

def keepliving(sec=300):
	t1=threading.Thread(target=th_keepliving, args=(sec))

@app.route("/keepliving")
def endpoint_keepliving():
	print("keeplivingendpoint")
	time.sleep(25)
	return "keepliving"


def DCsend(message,name):
	print(name,": " , os.environ[name])
	discordWH=os.environ[name]
	data={"content":" "+str(message)+" "}
	requests.post(discordWH,data=data)
  
def job():
    print("JOB", datetime.datetime.now())
    DCsend("Job"+str(datetime.datetime.now()), "WHURL")


schedule.every().minute.at(":00").do(job)

@app.route("/")
def index():
  print("JOB", datetime.datetime.now())
  DCsend("Job"+str(datetime.datetime.now()), "WHURL")
  return "Job"+str(datetime.datetime.now())


def thread():
	minute_wait=8
	DCsend(str(minute_wait)+"スレッドの開始", "WHURL")
	for t in range (minute_wait*6):
		time.sleep(10)
		DCsend(str(t)+" Threading...", "WHURL")
	DCsend(str(minute_wait)+"スレッド完了", "WHURL")

@app.route("/test_threading")
def test_threading():
	print("test_keepliving")
	keepliving(500)
	# t1=threading.Thread(target=thread)
	# t1.start()
	# time.sleep(480)
	# DCsend("スレッド外", "WHURL")
	
	minute_wait=8
	DCsend(str(minute_wait)+"スレッドの開始", "WHURL")
	for t in range (minute_wait*6):
		time.sleep(10)
		DCsend(str(t)+" Threading...", "WHURL")
	DCsend(str(minute_wait)+"スレッド完了", "WHURL")

	return "test_threading"
