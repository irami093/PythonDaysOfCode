#Write a program to count the occurrences of a specific character in a string

sample_string = input("Enter a string:")

selected_char = input("Enter character to be counted:")

selected_char_count = sample_string.count(selected_char)

print("The character selected occurs", selected_char_count, "times.")
