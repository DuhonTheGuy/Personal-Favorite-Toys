import numpy as np

def main():
	matrix, results = userInput()
	invMatrix = np.linalg.inv(matrix)
	print(invMatrix.dot(results))



def userInput():
	print("Please input the number of variables you have. Note: The same number is used for the number of equations.")
	try:
		n = int(input())
	except:
		print("Error: Please input a number")
		return 1

	matrix = []

	print("Input the lines of coefficients (numbers multiplying the variables) of your system, separated by a space.")

	for i in range(n):
		matrix.append([int(j) for j in input().split()])

	print("Input now the first, second, third, ..., nth result of the linear equations, separated by comma and space.")

	results = [int(i) for i in input().split()]

	return matrix, results

main()