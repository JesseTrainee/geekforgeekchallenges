# Given an Integer n, find the reverse of its digits.
# Examples:
# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.
def reverse_digits(num):
    str_num = str(num)
    num_arr = list(str_num)
    num_arr.reverse()
    return int(''.join(num_arr))

print(reverse_digits(315))