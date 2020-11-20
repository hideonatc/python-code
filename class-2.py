class ac:
	def __init__(self,name,account,withdraw,deposit):
		self.name = name
		self.account = account
		self.withdraw = withdraw
		self.deposit = deposit
i = ac(input(),input(),int(input()),int(input()))
print("Account Number:",i.name,"Account Name:",i.account)
print(i.withdraw-i.deposit)