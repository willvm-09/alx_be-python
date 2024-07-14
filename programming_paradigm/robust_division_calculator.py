def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    else: 
        print(f"The result of the division is {result}")
    finally:
        print(f"Division execution complete.")
    
    