while 1==1 :
	a = int(input("> "))
	s = 0
	for i in range (pow(10,a-1),pow(10,a)-1):
		s+=i
		print(i,'+',end="")
	print(pow(10,a)-1,"=",s+pow(10,a)-1)