def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name}, and I am {age} years old."

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if not numbers:
        return 0, None, None 
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, maximum, minimum

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    high_scorers = [name for name, score in students_dict.items() if score > 80]

    return high_scorers 

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements =set(list1) & set(list2)

    return common_elements 

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    operations = {
        "addition": a + b,
        "subtraction": a - b, 
        "multiplication": a * b,
        "division": a / b if b !=0 else "undefined"
    }

    return operations

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    operations = {
        "AND": x and y,
        "OR": x or y,
        "NOT_x": not x,
        "NOT_y": not y 
    }

    return operations 

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    operations = {
        "AND": a & b,
        "OR": a | b,
        "XOR": a ^ b,
        "NOT_a": ~a,
        "NOT_b": ~b,
        "left_shift_a": a << 1,
        "left_shift_b": b << 1,
        "right_shift_a": a >> 1,
        "right_shift_b": b >> 1,
    }

    return operations 