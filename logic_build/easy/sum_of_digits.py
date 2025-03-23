# Given a number n, find the sum of its digits.
# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21
def sum_digits(num):
    str_num = str(num)
    digits = list(str_num)
    result = 0
    for n in digits:
        result += int(n)
    return result

print(sum_digits(687))