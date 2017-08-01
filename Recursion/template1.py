"""Example function"""
def recursion_function(num):
    """Recursively print"""
    # ending condition
    if num == 0:
        return
    print num
    # call itself
    recursion_function(num - 1)
