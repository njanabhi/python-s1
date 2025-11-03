def num1(n, even, odd):
    if n % 2 == 0:
        return even
    else:
        return odd

n = int(input("Enter the number: "))
even_message = "Even"
odd_message = "Odd"

result = num1(n, even_message, odd_message)
print("The number is:", result)
