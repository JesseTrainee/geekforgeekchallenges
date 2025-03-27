# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.

# Examples:

# Input : x1, y1 = (3, 4)
#            x2, y2 = (7, 7)
# Output : 5

from math import pow, sqrt

def get_distance(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

res = get_distance(3, 4, 7, 7)
print(res)
res = get_distance(3, 4, 4, 3)
print(res)