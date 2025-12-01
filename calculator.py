while True:
    try:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")
        if operation.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break
            if operation not in ('+','-','*','/'):
                print("Invalid operation, please try  again.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        print(f"\n The result is: {result} \n")

    except ValueError:
        print("Invalid input, please enter numeric values.")
