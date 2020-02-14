import pdb
import requests
import boto3
import json
import os, time
import datetime

with open('dummy.json') as data:
    dummy_json = json.load(data)
for deploy in dummy_json:
    print(deploy)
    r = requests.post("https://i9dpeqt362.execute-api.ap-southeast-2.amazonaws.com/default/test_1", json=deploy)
    r.raise_for_status()
