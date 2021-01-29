# by Bekzat
cars = ["Toyota", "Volvo", "Ford"]
cars.append("Tesla") # adding "Tesla"
for x in cars:
	print(x)
cars.pop(1) # deleting "Volvo" - the second element
cars.remove("Ford")
print("\n")
for x in cars:
	print(x)