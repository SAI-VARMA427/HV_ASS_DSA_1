# Question 4:
# Write a program to check whether a String is a palindrome or not.
# Note: A Palindrome String is a string that is the same as the reverse.
# Example: LOL, MADAM.

# example 1
def is_palindrome(string):
    return string == string[::-1]

string = "LOL"
result = is_palindrome(string)
print(result)



# example 2


def is_palindrome(string):
    return string == string[::-1]

string = "MADAM"
result = is_palindrome(string)
print(result)
