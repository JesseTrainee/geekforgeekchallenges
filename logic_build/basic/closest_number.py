def closest_number(num1, num2):
    # por que ele não está incluindo o num2 * 10?
    array = [n for n in range(num2, num2 * 10 + 1) if n % num2 == 0]
    print(array)
    if num1 in array:
        return num1


closest_number(-15, 6)

# res = closest_number(13, 4)
# print(res)
# print(res)