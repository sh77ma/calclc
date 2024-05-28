import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py [number1] [operation] [number2]")
        sys.exit(1)

    num1 = float(sys.argv[1])
    operation = sys.argv[2]
    num2 = float(sys.argv[3])

    if operation == '+':
        print(addition(num1, num2))
    elif operation == '-':
        print(subtraction(num1, num2))
    else:
        print("Invalid operation. Please enter '+' or '-'.")

if __name__ == "__main__":
    main()
