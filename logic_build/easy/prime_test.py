# Given a positive integer, check if the number is prime or not.
# A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Examples of the first few prime numbers are {2, 3, 5, …}
# Examples :
# Input:  n = 11
# Output: true
def is_prime(num):
    if num <= 0:
        return False
    result = [n for n in range(1, num + 1) if num % n == 0]
    return len(result) == 2


res = is_prime(11)
print(res)