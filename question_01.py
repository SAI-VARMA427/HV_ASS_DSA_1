# Question 1:
# Write a program to rotate a given array by N steps in the clockwise direction

# Sample input one
# Array:- 3,1,2,5,7
# N:- 2
# Sample output one
#  5,7,3,1,2

# Sample input Two
# Array:- 1,2,3,4,5
# N:- 1
# Sample output two
#  5,1,2,3,4


# example 1
def rotate_array(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

arr = [3, 1, 2, 5, 7]
rotated_arr = rotate_array(arr, 2)
print(rotated_arr)


# example 2

def rotate_array(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]

arr = [1, 2, 3, 4, 5]
rotated_arr = rotate_array(arr, 1)
print(rotated_arr)

