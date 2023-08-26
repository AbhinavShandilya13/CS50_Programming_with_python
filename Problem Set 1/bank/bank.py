inp = input("write your greeting here: ")
inp = inp.lower()
if "hello" in inp:
    print("$0")
elif "h" in inp[0]:
    print("$20")
else:
    print("$100")