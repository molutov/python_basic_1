# 1
print(abs(-1))

# 2
print(all(True, True))

# 3
print(any(False, True))

# 4
print(ascii("name")) # for strange symb.

# 5
print(bin(24)) # to binary

# 6
print(bool(1))

# 7
print(bytearray(4))
print(bytearray("test", "utf-8"))

# 8
print(bytes(5))

# 9
def x():
    a = 5
print(callable(x)) # is it function

# 10
print(chr(60))

# 11
print(compile("print(1)", "test", "eval"))

# 12
print(complex("3 + 5j"))

# 13
class Person:
    name = "beka"
    age = 18
    country = "KZ"
delattr(Person, "age")

# 14
x = divmod(5, 2)
print(x)

# 15
x = ("apple", "banana")
y = enumerate(x, 10) # from 10
print(list(y))

# 16
# filter

# 17
x = format(0.5, "%") # formatting
print(x)

# 18
list = [1, 2, 3, 4]
x = frozenset(list)
print(x)

# 19
class Person:
    name = "beka"
    age = 18
p = Person()
p2 = Person()
x = getattr(Person, "age")

p2.name = "Kari"
print(p.name)
print(p2.name)

# 20
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict_2 = {
    "brand": "Ford_2",
    "model": "Mustang_2",
    "year": 1962
}
for i1, i2 in zip(thisdict.items(), thisdict_2.items()):
    if i1 == i2:
        print("same")
    else:
        print("not same")
# for k, v in thisdict.items():
#     print(k, v)
# for k in thisdict.iteritems():
#     print(k)

# 21
# zip
a = ("apple", "banana")
b = ("apple_2", "banana_2")
x = zip(a, b)
print(tuple(x))

# 22
x = globals()
print(x)

# 23
x = hex(255)
print(x)

# 24
x = ("apple", "banana")
print(id(x))

# 25
p = 2.5
x = isinstance(p, int)
print(x)

# 26
#
#
# python iterators
#
#

# 27
def my_func(a, b):
    return a + b
x = map(my_func, ("apple"), ("apple_2"))
print(x)

# 28
print(ord("k"))

# 29
x = round(5.7684, 2)
print(x)

# 30
a = ("a", "b", "c", "d", "e")
# slice
