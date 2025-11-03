import math
def is_all_even(n):
    for digit in str(n):
        if int(digit) % 2 != 0:
            return False
    return True
def even_digit_perfect_squares(start, end):
    result = []
    for num in range(start, end + 1):
        root = int(math.sqrt(num))
        if root * root == num and is_all_even(num):
            result.append(num)
    return result

numbers = even_digit_perfect_squares(1000, 9999)
print("4-digit even-digit perfect squares:", numbers)