def sumOfSquares(m):
	return sum([n ** 2 for n in range(1,m + 1)])

def squareOfSum(m):
	return sum(n for n in range(1, m+1)) ** 2

print(squareOfSum(100) - sumOfSquares(100))
