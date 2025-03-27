# Given two positive numbers x and y, check if y is a power of x or not.
# Examples :

# Input:  x = 10, y = 1
# Output: True
# x^0 = 1

def check_power(x, y):
    tmp = y
    while tmp > 1:
        tmp = tmp / x

    return tmp == 1

res = check_power(10, 1000)
print(res)
res = check_power(6, 216)
print(res)
res = check_power(2, 7)
print(res)