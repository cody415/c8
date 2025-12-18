# Program to find correct mean when a number was misread

# Given data
n = 40
mean = 38

# Calculate wrong sum
wrong_sum = n * mean

# Misread number
wrong_value = 36
correct_value = 56

# Correct sum
correct_sum = wrong_sum - wrong_value + correct_value

# Correct mean
correct_mean = correct_sum / n

print("Wrong mean:", mean)
print("Correct mean:", correct_mean)
