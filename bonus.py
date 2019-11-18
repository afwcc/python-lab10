def recordnumber():
    number = input("please enter the number between 1 to 24")
    if number =="q":
        quit(0)
    elif number > 24:
        input("please enter the number between 1 to 24")

recordnumber()