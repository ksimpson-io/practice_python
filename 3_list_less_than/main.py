# write a program that prints out all the elements of the list that are less than 5.
# make a new list that has all the elements less than 5 from this list in it and print out this new list.
# ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

def start():
    user_num = int(input("Enter a number: "))
    input(f"Goal: Find all elements less than {user_num}")
    ans = input("Do you want a list? (y) or one by one (n)?")

    if (ans == "y"):
        for idx, num in enumerate(a):
            if (num < user_num):
                new_list.append(num)
        print(new_list)
        
    else:
        for i in a:
            if (num < user_num):
                print(i)

start()
