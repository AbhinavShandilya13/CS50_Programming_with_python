inp = input("write down your inp: ")
x, y, z = inp.split(" ")
x = float(x)
z = float(z)

if y == "+":
    result = x+z
if y == "-":
    result = x-z
if y == "/":
    result = x/z
if y == "*":
    result = x*z
print(result )