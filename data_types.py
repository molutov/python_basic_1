# by Bekzat
x = "Hello World"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple", "banana", "cherry"] # dynamic
print(type(x))
x = ("apple", "banana", "cherry") # static
print(type(x))
x = range(5)
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple", "banana", "cherry"} #set
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
# frozenset is just an immutable version of a set object
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
# function returns a memory view object from a specified object
print(type(x))