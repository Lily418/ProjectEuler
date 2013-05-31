import math

def getFactors(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		x = n / i
		
		if(x%1 == 0):
			return (i,int(x))
	
	return None


def findFactors(n):
	factors = [n]
	primeFactors = []

	while len(factors) > 0:
		factor = factors.pop()
		newFactors = getFactors(factor)

		if(newFactors == None):
			primeFactors.append(factor)
		else:
			factors.append(newFactors[0])
			factors.append(newFactors[1])

	return primeFactors

def findHighestFactor(n):
	return findFactors(n)[0]

print(findHighestFactor(600851475143))
