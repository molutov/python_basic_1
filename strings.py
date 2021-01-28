# by Bekzat
string = "hello my friends!"
print(string)
print(string[0])
string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(string)
print(len(string))
if "tempor" in string:
	print("tempor is here!")
if "beka" not in string:
	print("beka is not here!")