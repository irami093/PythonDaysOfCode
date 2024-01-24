#Write a program to print the multiplication table of a given number

given_number = int(input("Enter a random number:"))


print("Multiplication table for", given_number)
for i in range(1, 15):
    print(i*given_number)
