c=ord('1')-ord('*')
while 1==1 :
	s=input()
	l=len(s)
	ans=""
	for i in s:
		ans+=chr(ord(i)-c)

	print("%s"%(ans))