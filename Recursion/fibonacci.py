def fibonacci(num):
    # Condition of ending recursion
    if num <= 2:
        return 1
    # fibonacci formula
    return fibonacci(num - 1) + fibonacci(num - 2)

# TEST
print 'TEST:'
print fibonacci(6)
