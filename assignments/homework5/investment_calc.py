from tkinter import *

class InvestmentCalculator:
	def __init__(self):
		window = Tk()
		window.title("Investment Calculator")
		Label(window, text="Investment Amount").grid(row=1, column=1, sticky=W)
		Label(window, text="Years").grid(row=2, column=1, sticky=W)
		Label(window, text="Annual Interest Rate").grid(row=3, column=1, sticky=W)
		Label(window, text="Future Value").grid(row=4, column=1, sticky=W)

		self.investmentAmtVar = StringVar()
		Entry(window, textvariable=self.investmentAmtVar, justify=RIGHT).grid(row=1, column=2)

		self.numberOfYearsVar = StringVar()
		Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)

		self.annualInterestRateVar = StringVar()
		Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=3, column=2)

		self.futureValVar = StringVar()
		Label(window, textvariable=self.futureValVar).grid(row=4, column=2, sticky=E)


		Button(window, text="Calculate", command=self.computeValue).grid(row=6, column=2, sticky=E)

		window.mainloop()

	def computeValue(self):
		futureValue = float(self.investmentAmtVar.get()) * (1 + float(self.annualInterestRateVar.get()) / 12)**(float(self.numberOfYearsVar.get()) * 12)
		self.futureValVar.set(format(futureValue, "10.2f"))

InvestmentCalculator()