# Fibonacci number generator 

for n in range(0, 11):
if n==0:
	f[n] = 1;
	f[n+1]=1;
 else:
	f[n+2] .append(f[n+1] + f[n])

print(f[4])
