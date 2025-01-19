def function_with_uncommon_error_solution(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
        return "Cannot divide non-numeric types"
    try:
        result = a / b
        return result
    except TypeError:
        return "Type Error"
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = function_with_uncommon_error_solution([1,2], [3,4])
print(result)  # Output: Cannot divide non-numeric types

result = function_with_uncommon_error_solution(10, 0)
print(result) # Output: Cannot divide by zero

result = function_with_uncommon_error_solution(10,2)
print(result) # Output: 5.0

result = function_with_uncommon_error_solution(10, "a")
print(result) # Output: Type Error