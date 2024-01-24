#Write a program to reverse a given string

x = input("Input a string:")

def my_string(x):
    if len(x) == 0:
        return "No string detected."
    else:
        return x[::-1]

my_string_reversed = my_string(x)

print(my_string_reversed)