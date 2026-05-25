# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

def start():
    input("             IS YOUR NUMBER EVEN OR ODD?                 ")
    input("             LETS FIND OUT               ")

    num = int(input("Enter a number: "))

    if (num % 4 == 0):
        print("THIS ONE IS ACTUALLY DIVISIBLE BY 4")
    elif (num % 2 == 0):
        print("THIS NUMBER IS EVEN")
    else:
        print("THIS NUMBER IS ODD")


start()
