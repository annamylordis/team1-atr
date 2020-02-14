import pdb
import requests
import boto3
import json
import os, time
import datetime

metadata = {}

aws_access_key_id="AKIAS5I3NNHKQVKICKEL"
aws_secret_access_key="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"    

response = requests.get("http://169.254.169.254/latest/meta-data/public-hostname")
metadata["hostname"] = response.text
data = {}
with open("build.properties") as f:
	for i in f:
		key, val = i.split("=")
		data[key.strip()] = val.strip()
date = data["BUILD_DATE"]
version = data["FULL_VERSION"]

instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id")

time_stamp = os.path.getmtime("installation.log")
print(time_stamp)
print(dir(datetime.datetime))
print(type(time_stamp))

#time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
#time_stamp = str(time_stamp)
print(str(time_stamp*1000))
#time_stamp = datetime.datetime.strptime(time_stamp, "%d %b %y")

metadata["build-date"] =  date
metadata["package-version"] = version   
metadata["instance-id"] = instance_id.text     
metadata["time-stamp"] = time_stamp*1000
metadata["client-name"] = "ANZ"

print(metadata)

json_metadata = json.dumps(metadata)
print(json_metadata) 
r = requests.post("https://i9dpeqt362.execute-api.ap-southeast-2.amazonaws.com/default/test_1", json=metadata)

print(r.status_code)
print(r.json())

print(response.text)
print(date)
print(version)
