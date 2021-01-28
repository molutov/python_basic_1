# by Bekzat
# Add a placeholder where you want to display the price
price = 1000
txt = "The price is {} tenge"
print(txt.format(price))
# Format the price to be displayed as a number with two decimals
txt = "The price is {:.2f} tenge"
print(txt.format(price))
# If you want to use more values:
quantity = 5
name = "cheese"
price = 50
order = "I want {} pieces of {} for {:.2f} tenge"
print(order.format(quantity, name, price))
# You can use index numbers:
order = "I want {0} pieces of {1} for {2:.2f} tenge"
print(order.format(quantity, name, price))
# Also, if you want to refer to the same value more than once, use the index number:
age = 18
name = "Bekzat"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# Named indexes:
order = "I love {carname}, it is {model}."
print(order.format(carname = "Tesla", model = "a model S"))

