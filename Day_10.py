#Write a program to remove duplicates from a list

sample_list = [1, 1, 2, 3, 4, 5, 5, 6, 6, 7]

def remove_dupes(list):
    return set(list)

unique_sample_list = remove_dupes(sample_list)
print(unique_sample_list)