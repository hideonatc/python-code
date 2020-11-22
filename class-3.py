class ac:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
i = ac(input(),input())
if not i.salary.isnumeric():
	print("你輸入的salary應該要是整數喔！")
else:
	try:
		x = 100/(int(i.salary)-1)
	except Exception as e:
		print("捕捉錯誤資訊:"+str(e))
		print("萬能用法： 當不知道會發生什麼錯誤時的捕捉錯誤方法")
	else:
		print("正確執行 :\nHello",i.name,"\n你的薪水需要個"+str(100/(int(i.salary)-1))+"月來完成付款")
print("程式結束\n======================================")