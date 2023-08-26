Inp = input("what is your input:")
if Inp.strip() == "42":
    print ("Yes")
elif Inp.lower().strip() == "forty-two":
    print("Yes")
elif Inp.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")