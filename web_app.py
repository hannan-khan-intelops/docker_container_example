from flask import Flask
import pandas as pd
import .app

app = Flask('docker_example_2')

@app.route('/')
def home():
	df = pd.DataFrame()
	df['FizzBuzz'] = app.fizzbuzz()
	print(df)