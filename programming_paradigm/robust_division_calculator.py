def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
    except ZeroDivisionError:
        if denominator == 0:
            return f"Error: Cannot divide by zero."
    except ValueError:
        return f"Error: Please enter numeric values only."  
    else:
        return f"The result of the division is {result}"  
    
        