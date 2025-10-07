num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter choice (+,-,*,/): ")

if choice == '+':
    def add(a, b):
        return a + b
    print(f"Result: {add(num1, num2)}")
elif choice == '-':
    def subtract(a, b):
        return a-b
    print(f"Result: {subtract(num1, num2)}")
elif choice == '*':
    def multiply(a, b):
        return a*b
    print(f"Result: {multiply(num1, num2)}")
elif choice == '/':
    def divide(a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a/b
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")
