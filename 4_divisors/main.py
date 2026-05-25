# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

def start():
    num_list = []
    user_num = int(input("Enter a number: "))

    input(f"PRINTING OUT ALL DIVISORS OF {user_num}...")

    for x in range(1, user_num+1):
        if (user_num % x == 0): num_list.append(x)

    print(num_list)


start()
