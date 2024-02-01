def f(x):
	return x**3+8

def main():
	x_value = 9
	result = f(x_value)

	print("Result:", result)

	if result > 27:
		print("YAY!")

if __name__ == "__main__":
	main()