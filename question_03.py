# Question 3 : 
# Write a program to find the element with the highest frequency in the list.
# Sample_input :[1,2,4,3,2,4,2,5,7,2]
# Sample_output :2


def highest_frequency(arr):
    frequency = {}
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return max(frequency, key=frequency.get)

arr = [1, 2, 4, 3, 2, 4, 2, 5, 7, 2]
most_frequent = highest_frequency(arr)
print(most_frequent)
