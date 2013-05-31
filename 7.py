primes = {x : True for x in range(2, 500000)}

#Prime Sieve
for k,v in primes.items():
	if v:
		for i in range(k * 2, len(primes) + 2, k):
			primes[i] = False

primeCount = 0
for i in primes.keys():
	if primes[i]:
		primeCount+=1
	if primeCount == 10001:
		print(i)
		break;
