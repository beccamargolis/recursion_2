# Write rFib(num). Recursively compute and return numth Fibonacci value.
# As earlier, treat first two (num = 0, num = 1) Fibonacci vals as 0 and 1. 

def rFib(num):
    if num < 2:
        return num
    return rFib(num-2) + rFib(num-1)

# Write function rTrib(num) to mimic Fibonacci, adding previous three values instead of two.
# First three Tribonacci numbers are 0, 0, 1, so rTrib(3) = 1 (0+0+1); rTrib(4) = 2 (0+1+1); rTrib(5) = 4 (1+1+2); rTrib(6) = 7 (1+2+4).
# Handle negatives and non-integers appropriately and inexpensively.

def rTrib(num):
    pass
# The Ackermann Function

# Zibonacci