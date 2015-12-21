from flask import Flask, request, session, g, redirect, url_for, \
	 abort, render_template, flash
import os
import md5
from time import time
from datetime import timedelta
import urllib
import json
import datetime
from urllib import urlencode

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

NEXMO_API = os.environ.get('NEXMO_KEY')
NEXMO_SECRET_KEY = os.environ.get('NEXMO_SECRET')
BRAND_NAME = 'Your verification '
VERIFY_DURATION = 5 * 60 
BASE_URL = 'https://api.nexmo.com'

if 'VERIFY_DURATION' in os.environ:
	VERIFY_DURATION = int(os.environ.get('VERIFY_DURATION')) * 60 

	
def check_number(To):
	if To is None or To.strip() is '':
		return response_jsong(401, 'Please enter a Phone Number.', 'error')
	if (To is None) or (len(To)<=10) or (not To.isdigit()):
		return reponse_jsong(401, 'Please enter a valid Phone Number.', 'error')
	return True


def reponse_jsong(status, msg, stats):
	reps_j = {}
	reps_j = {'status_code':status, 'msg':msg, 'status':stats}
	return json.dumps(reps_j)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
	To = request.values.get("dst")
	Status  = check_number(To)
	if Status == True:
		rest_url = BASE_URL + '/verify/json'
		data_set = {'api_key':NEXMO_API,
		'api_secret':NEXMO_SECRET_KEY,
		'brand':BRAND_NAME,
		'pin_expiry':VERIFY_DURATION,
		'number':str(To)} 
		content = urllib.urlopen(rest_url+ '?' + urlencode(data_set)).read()
		return content
	return Status

@app.route('/validate', methods=['GET'])
def validate():
	code = request.values.get('code')
	req_id = request.values.get('req_id')
	rest_url = BASE_URL + '/verify/check/json'
	data_set = {'api_key':NEXMO_API,
	'api_secret':NEXMO_SECRET_KEY,
	'request_id':req_id,
	'code':code}
	content = urllib.urlopen(rest_url + '?' + urlencode(data_set)).read()
	return content

@app.route('/status', methods=['GET'])
def status():
	req_id = request.values.get('req_id')
	rest_url = BASE_URL + '/verify/search/json'
	data_set = {'api_key':NEXMO_API,
	'api_secret':NEXMO_SECRET_KEY,
	'request_id':req_id}
	content = urllib.urlopen(rest_url + '?' + urlencode(data_set)).read()
	return content	
	



if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)