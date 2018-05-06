from stock import Stock

intc = Stock()
intc.setName("Intel Corporation")
intc.setSymbol("INTC")
intc.setPreviousClosingPrice(20.5)
intc.setCurrentPrice(20.35)
print("Price change from today and yesterday: ", intc.getChangePercent())

