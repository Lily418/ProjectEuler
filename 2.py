cache = {}

def fib(n):
	if n in cache:
		return cache[n]
	
	if n == 0 or n == 1:
		return n
	else:
		m = fib(n-1) + fib(n-2)
		cache[n] = m
		return m

def isEven(n):
	return n % 2 == 0

def sumFib(m):
	total = 0
	lastNum = 0
	n = 2
	
	while(lastNum < m):
		
		if isEven(lastNum):		
			total += lastNum

		lastNum = fib(n)
		n += 1

	return total

print(sumFib(4000000))
