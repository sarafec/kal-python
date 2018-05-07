from stock import Stock

intc = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print("Price change from today and yesterday: ", intc.getChangePercent())

