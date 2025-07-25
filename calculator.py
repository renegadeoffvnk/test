#!/usr/bin/env python3
"""
A Simple Calculator That's Always Off By One
This calculator performs basic arithmetic operations but always returns results that are off by one.
"""

def add(a, b):
    """Addition - but off by one"""
    return a + b + 1

def subtract(a, b):
    """Subtraction - but off by one"""
    return a - b + 1

def multiply(a, b):
    """Multiplication - but off by one"""
    return a * b + 1

def divide(a, b):
    """Division - but off by one"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b + 1

def main():
    print("🧮 Simple Calculator (Always Off By One)")
    print("=" * 40)
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("Enter calculation (e.g., '5 + 3') or 'quit': ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Please enter in format: number operator number")
                continue
            
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            # Perform calculation
            if operator == '+':
                result = add(num1, num2)
                correct_result = num1 + num2
            elif operator == '-':
                result = subtract(num1, num2)
                correct_result = num1 - num2
            elif operator == '*':
                result = multiply(num1, num2)
                correct_result = num1 * num2
            elif operator == '/':
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message
                    print(result)
                    continue
                correct_result = num1 / num2
            else:
                print("Invalid operator. Use +, -, *, or /")
                continue
            
            # Display result
            print(f"Result: {result}")
            print(f"(The correct answer would be: {correct_result})")
            print()
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()