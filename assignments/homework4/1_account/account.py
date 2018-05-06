class Account:
	def __init__(self):
		self.__id = 0
		self.__balance = 0
		self.__annualInterestRate = 0

		# accessor methods
		def getId(self):
			return self.__id

		def getBalance(self):
			return self.__balance

		def getAnnualInterestRate(self):
			return self.__annualInterestRate


		# mutator methods
		def setId(self, num):
			self.__id = num

		def setBalance(self, amt):
			self.__balance += amt

		def setAnnualInterestRate(self, rate):
			self.__annualInterestRate = rate


		# methods
		def getMonthlyInterestRate(self):
			return self.getAnnualInterestRate() / 12

		def getMonthlyInterest(self):
			return (self.__balance * self.getMonthlyInterestRate())/100

		def withdraw(self, amt):
			self.setBalance(amt)
			print("You've withdrawn ", amt, " from your account. You have a balance of ", self.getBalance())


		def deposit(self, amt):
			self.setBalance(amt)
			print("You've deposited ", amt," You have a balance of ", self.getBalance())
