inp = input("Write the file name here: ")
inp = inp.lower()
if ".jpg" in inp:
    print("image/jpeg")
elif ".gif" in inp:
    print("image/gif")
elif ".jpeg" in inp:
    print("image/jpeg")
elif ".png" in inp:
    print("image/png")
elif ".pdf" in inp:
    print("application/pdf")
elif ".txt" in inp:
    print("text/plain")
elif ".zip" in inp:
    print("application/zip")
else:
    print("application/octet-stream")