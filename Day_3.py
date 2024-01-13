#Write a function to count the number of vowels in a given string

sample_text = input("Please enter a word or phrase:")

count = 0

for character in sample_text:
    if (character in "aAeEiIoOuU"):
        count +=1
print("Count:", count)

