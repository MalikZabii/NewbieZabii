def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        if operation == '+':
            print("Result:", add(a, b))
        elif operation == '-':
            print("Result:", subtract(a, b))
        elif operation == '*':
            print("Result:", multiply(a, b))
        elif operation == '/':
            print("Result:", divide(a, b))
        else:
            print("Invalid operation!")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()
