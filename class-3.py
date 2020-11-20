class ac:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
i = ac(input(),0)
s = input()
if not s.isnumeric():
	print("你輸入的salary應該要是整數喔！")
else:
	print("正確執行 :\nHello",i.name,"\n你的薪水需要個"+(100/(int(s)-1))+"月來完成付款")
try:
	s = int(s)
except Exception as e:
	print("捕捉錯誤資訊:"+str(e))
print("程式結束\n======================================")