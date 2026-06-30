try:
    numerator = float(input("Enter a number: "))
    denominator = float(input("Enter another number: "))
    result = numerator / denominator
    print(f"result : {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter valid numeric values.")