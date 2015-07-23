# -*- config:utf-8 -*-

from flask import Flask
from config import default

app = Flask(__name__)
app.config.from_object('config.default')
app.config.from_envvar('SOCIAL_MONITORING_SETTINGS', silent=True)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()
