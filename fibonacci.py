def fib(n, M = {}):
	if n in M: return M[n]
	if n <=2: return 1
	M[n] = fib(n-1,M) +fib(n-2,M)
	return M[n]
print(fib(70))

