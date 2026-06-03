# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def start():
    word = input("Enter a word: ")
    backwards = ("".join(reversed(word)))

    pal = "is" if (word == backwards) else "is NOT"
    print(f'{word} {pal} a palindrome')

start()
