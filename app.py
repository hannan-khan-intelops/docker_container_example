"""This is a sample app for the docker container example.
It calculates the fizzbuzz, and thats it."""

import pandas as pd


def fizzbuzz(max_n: int = 100) -> []:
    """
    Goes through n numbers and sees if they are divisible by
    3, 5, or both.
    Returns a list of the results.
    """
    output = []
    for i in range(max_n):
        if i % 15 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output


if __name__ == "__main__":
    # Creates a dataframe and populates a column
    # with the results of fizzbuzz().

    df = pd.DataFrame()
    df["FizzBuzz"] = fizzbuzz()
    print(df)
