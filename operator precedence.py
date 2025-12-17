# Program to understand operator precedence

# Example expression
result1 = 10 + 5 * 2        # Multiplication has higher precedence than addition
result2 = (10 + 5) * 2      # Parentheses change the order
result3 = 100 / 5 + 2       # Division happens before addition
result4 = 2 ** 3 * 2        # Exponentiation has higher precedence than multiplication
result5 = 10 - 3 + 2        # Left to right for same precedence operators
result6 = 10 > 5 and 5 < 8  # Comparison before logical AND

# Display results
print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)
print("100 / 5 + 2 =", result3)
print("2 ** 3 * 2 =", result4)
print("10 - 3 + 2 =", result5)
print("10 > 5 and 5 < 8 =", result6)
