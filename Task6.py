class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 < 0 or num2 < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")

        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except NegativeNumberError as e:
        print("Custom Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)

    else:
        print(f"Result: {result}")

    finally:
        print("Execution completed.")

divide_numbers()
