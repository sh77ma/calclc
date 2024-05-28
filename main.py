def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2

def main():
    print("Console Calculator")
    print("Enter 'quit' to exit")

    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation == 'quit':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                print("Result:", addition(num1, num2))
            elif operation == '-':
                print("Result:", subtraction(num1, num2))
            elif operation == '*':
                print("Result:", multiplication(num1, num2))
            elif operation == '/':
                print("Result:", division(num1, num2))
            else:
                print("Invalid operation. Please enter '+', '-', '*', or '/'.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
