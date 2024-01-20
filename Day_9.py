#Write a program to check if a number is even or odd.

sample_number = int(input("Enter a random number:"))

def even_or_odd_number(sample_number):
    if sample_number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


even_or_odd_number(sample_number)