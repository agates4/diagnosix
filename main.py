from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from engine.find_words import get_data
from engine.db import SQLConnection
import json
import base64
import requests
# import subprocess
# import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_page():
	return "hei"

@app.route('/speech', methods=['GET', 'POST'])#processes text
def interpret_string():
	data=request.get_json(force=True)
	text=data["speech"].lower()
	tempy=SQLConnection().send_data(text)
	the_data=get_data().send_json(text)
	print data
	
	print "#######################"
	if the_data!=False:
		other=json.loads(the_data)
		other["YT"]=tempy
		the_data=json.dumps(other)
                return (the_data)
                return str(other)
		return str(other["ID"])
	else:
		return text
	
@app.route('/speech_get', methods=['GET', 'POST'])#call to get data from db
def junk():
	return SQLConnection().get_data()
	
@app.route('/token', methods=['GET', 'POST'])
def send_token():
    key = "Authorization"
    value = "Bearer agates10@kent.edu:4Gy54wodlr8+r0HksBaxmg=="
    url = "https://sandbox-authservice.priaid.ch/login"
    # postHeaders = [(key, value)]
    headers = {'Authorization': 'Bearer agates10@kent.edu:4Gy54wodlr8+r0HksBaxmg=='}
    r = requests.post(url, headers=headers)
    return r.text


if __name__ == "__main__":
    app.run(debug=True)

app.config['SERVER_NAME'] = 'geczy.tech'
app.run(
    host=app.config['SERVER_NAME'],
    port=5000,
    debug=True,
)


