def func(n = 5):
	if n==1 : 
		return 1
	else :
		return func(n-1)+n
a = 10
print(func(a))
print(func())