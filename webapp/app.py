import os
from flask import Flask,jsonify
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def home():

	res = {
		"appName": os.getenv("appName")
	}

	return jsonify(res)


if __name__ == '__main__':
	app.run(
			host="0.0.0.0",
			port=5000,
			debug=True
		)