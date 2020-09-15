while 1==1 :
	a,b = eval(input("> "))
	i = a
	s = 0
	for i in range (0,b-a):
		s+=a+i
		print(a+i,"+",end="")
	print(b,"=",s+b)