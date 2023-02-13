# Question 2 : 
# Write a program to print duplicate elements of a list.
# Sample_input : [1,1,2,3,3,4,5,6,6]
# Sample_ouptut : 1,3,6


def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for element in arr:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)
    return duplicates

arr =  [1, 1, 2, 3, 3, 4, 5, 6, 6]
duplicates = find_duplicates(arr)
print(duplicates)
