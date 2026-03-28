#creating a dictionary

fruit_prices = {"apple":1.50,"banana":.75,"orange":2.00}

#accessing a value
print(fruit_prices["banana"])

#changing a value
fruit_prices["banana"] = .50

print(fruit_prices["banana"])

#adding an item
fruit_prices["pear"] = 1.25

print(fruit_prices)

#deleting an item
del fruit_prices["orange"]

print(fruit_prices)

#listing the keys
print(list(fruit_prices.keys()))

#listing the values
print(list(fruit_prices.values()))

#listing the items
print(list(fruit_prices.items()))