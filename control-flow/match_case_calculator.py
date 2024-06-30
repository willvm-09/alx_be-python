num1 = int(input("Enter the first number:" ))
num2 = int(input("Enter the second number:" ))
operator = input("Choose the operation (+, -, *, /):" )

match operator:
    case "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    case "/":
        result = num1 / num2
        if num1 > 0 and num2 > 0:
            print(f"{num1} / {num2} = {result}")
        else:
            print("Cannot divide by zero.")
