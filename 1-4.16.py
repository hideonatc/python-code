while 1==1 :
	a = float(input("> "))
	print("=",int(a),"+","{:4.2f}".format(a-int(a)+0.001))