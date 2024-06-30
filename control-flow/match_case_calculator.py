num1 = int(input("Enter the first number:" ))
num2 = int(input("Enter the second number:" ))
operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        result1 = num1 + num2
        print("The result is", result1)
    case "-":
        result2 = num1 - num2
        print("The result is", result2)
    case "*":
        result3 = num1 * num2
        print("The result is", result3)
    case "/":
        if num1 > 0 and num2 > 0:
            result4 = num1 / num2
            print("The result is", result4)
        else:
            print("Cannot divide by zero.")
