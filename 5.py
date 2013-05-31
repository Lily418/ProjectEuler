import math

def getFactors(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		x = n / i
		
		if(x%1 == 0):
			return (i,int(x))
	
	return None

def findPrimeFactors(n):
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



def findLCM (n, m):
	primeFactorsOfN = findPrimeFactors(n)
	primeFactorsOfM = findPrimeFactors(m)
		
	maxOfFactorCount = []
	for i in {x for x in primeFactorsOfN + primeFactorsOfM}:
		maxOfFactorCount.append((i, max(primeFactorsOfN.count(i), primeFactorsOfM.count(i))))


	sumOfMaxFactors = 1	
	for pair in maxOfFactorCount:
		sumOfMaxFactors *= pair[0] ** pair[1]

	return sumOfMaxFactors

def findLCMOfList(l):
	lcm = l.pop()
	while(len(l) > 0):
		b = l.pop()
		lcm = findLCM(lcm, b)
	return lcm

print(findLCMOfList(list(range(1,21))))
	
