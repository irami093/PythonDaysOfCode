#Write a program to cheeck if a number is positive, negative, or zero

number_list = [0, 5, 10, -15, 20, -35, - 45, -75, 100]

count_of_positive_numbers = 0
count_of_negative_numbers = 0
count_of_zeros = 0

for number in number_list:
    if number > 0:
        count_of_positive_numbers +=1
    elif number < 0:
        count_of_negative_numbers += 1
    elif number == 0:
        count_of_zeros += 1
    else:
        print("Not a number!")

print("The total count of positive numbers is:", count_of_positive_numbers)
print("The total count of negative numbers is:", count_of_negative_numbers)
print("The total count of zeros:", count_of_zeros)