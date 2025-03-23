# Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series.
# Examples :

# Input : a1 = 2,  a2 = 3,  n = 4
# Output : 5
# Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 5th term is 5.
def n_term(a1, a2, n):
    r = a2 - a1
    an = a1 + (n - 1) * r
    return an
res = n_term(1, 3, 10)
print(res)