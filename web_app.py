import app as a
from flask import Flask
import pandas as pd

app = Flask('docker_example_2')

@app.route('/')
def home():
	""" Creates a dataframe, and populates the results from
	fizzbuzz().
	Returns a nice html string of the dataframe."""
	df = pd.DataFrame()
	df['FizzBuzz'] = a.fizzbuzz()
	return str(df.to_html())