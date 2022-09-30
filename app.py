import pandas as pd


def fizzbuzz(n: int = 100) -> List():
	"""
	Goes through n numbers and sees if they are divisible by
	3, 5, or both.
	Returns a list of the results.
	"""
	output = []
	for i in range(n):
		if i % 15 == 0:
			output.append("FizzBuzz")
		elif i % 3 == 0:
			output.append("Fizz")
		elif i % 5 == 0:
			output.append("Buzz")
		else:
			output.append(str(i))


if __name__ == '__main__':
	df = pd.Dataframe()
	df['FizzBuzz'] = fizzbuzz()
	print(df.head())