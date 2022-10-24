"""This is a web app for the docker container example.
It will calculate fizzbuzz. And display it in a UI."""

from flask import Flask
import pandas as pd

import app as a

app = Flask('docker_example_2')


@app.route('/')
def home():
    """Creates a dataframe, and populates the results from fizzbuzz().
    Returns a nice html string of the dataframe."""
    fizzbuzz_df = pd.DataFrame()
    fizzbuzz_df['FizzBuzz'] = a.fizzbuzz()
    return str(fizzbuzz_df.to_html())
