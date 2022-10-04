def fac(n):
	if n <= 1:
		return n
	else:
		return(fac(n-1) + fac(n-2))		
n = int(input())
for n in range(0,n):
		print(fac(n))
