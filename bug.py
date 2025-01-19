def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "Cannot divide strings"
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Uncommon error case: a and b are not numbers, but they are not strings either.
result = function_with_uncommon_error([1,2], [3,4])
print(result) # This will raise a TypeError because lists cannot be directly divided.