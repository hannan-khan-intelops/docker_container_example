import app as a
from flask import Flask
import pandas as pd

app = Flask('docker_example_2')

@app.route('/')
def home():
	df = pd.DataFrame()
	df['FizzBuzz'] = a.fizzbuzz()
	return str(df.head())