#You are given a cubic dice with 6 faces.
# All the individual faces have a number printed on them.
# The numbers are in the range of 1 to 6, like any ordinary dice.
# You will be provided with a face of this cube, your task is to guess the number
# on the opposite face of the cube.
# Ex:
# Input: n = 2
# Output: 5
# Explanation: For dice facing number 5 opposite face will have the number 2.

def guess_oposite_face(n):
    # a regra é que a face oposta sempre sera num - 7
        return abs(n - 7)

res = guess_oposite_face(2)
print(res)
res = guess_oposite_face(6)
print(res)