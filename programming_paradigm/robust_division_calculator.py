def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")

    try: 
        result2 = float(numerator) / float(denominator)
    except ValueError:
        print(f"Error: Please enter numeric values only.")
    else: 
        print(f"The result of the division is {result2}")
    finally:
        print(f"Division execution complete.")
    
    