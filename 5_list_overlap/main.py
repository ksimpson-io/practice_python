# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 44, 55, 7, 88, 67]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 67, 4, 23, 1231, 4534534, 131232, 3453453, 1132231, 3533, 55]
new = []
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.


def start():
    print(list(set(a) & set(b)))
    
start()
