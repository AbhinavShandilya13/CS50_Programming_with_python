def main():
    inp = input("What time is: ")
    time = convert(inp)
    if 7<=time<=8:
        print("Breakfast time")
    if 12<=time<=13:
        print("Lunch time")
    if 18<=time<=19:
        print("Dinner time")





def convert(time):
    hours, minutes = time.split(":")
    min =  float(minutes)/60
    return float(hours) + min



if __name__ == "__main__":
    main()