
import math
from datetime import datetime

history = []


def show_menu():
    print("\n" + "=" * 45)
    print("       ADVANCED PYTHON CALCULATOR")
    print("=" * 45)
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Modulus")
    print("6.  Power")
    print("7.  Floor Division")
    print("8.  Square")
    print("9.  Cube")
    print("10. Square Root")
    print("11. Percentage")
    print("12. Factorial")
    print("13. Sine (sin)")
    print("14. Cosine (cos)")
    print("15. Tangent (tan)")
    print("16. Logarithm (base 10)")
    print("17. Natural Logarithm")
    print("18. Show History")
    print("19. Clear History")
    print("0. Exit")
    print("=" * 45)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def record_result(operation, result):
    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "result": result
    })


def show_history():
    if not history:
        print("\nNo calculation history available.")
        return

    print("\n--- CALCULATION HISTORY ---")
    for index, item in enumerate(history, start=1):
        print(f"{index}. [{item['time']}] "
              f"{item['operation']} = {item['result']}")


def calculate():
    while True:
        show_menu()
        choice = input("Choose an option (0-19): ").strip()

        try:
            if choice == "0":
                print("\nThank you for using the calculator!")
                break

            elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                if choice == "1":
                    operation = f"{a} + {b}"
                    result = a + b

                elif choice == "2":
                    operation = f"{a} - {b}"
                    result = a - b

                elif choice == "3":
                    operation = f"{a} * {b}"
                    result = a * b

                elif choice == "4":
                    if b == 0:
                        print("Error: Cannot divide by zero!")
                        continue
                    operation = f"{a} / {b}"
                    result = a / b

                elif choice == "5":
                    if b == 0:
                        print("Error: Cannot calculate modulus by zero!")
                        continue
                    operation = f"{a} % {b}"
                    result = a % b

                elif choice == "6":
                    operation = f"{a} ** {b}"
                    result = a ** b

                else:
                    if b == 0:
                        print("Error: Cannot divide by zero!")
                        continue
                    operation = f"{a} // {b}"
                    result = a // b

            elif choice in ["8", "9", "10", "12", "13",
                            "14", "15", "16", "17"]:
                a = get_number("Enter a number: ")

                if choice == "8":
                    operation = f"{a} squared"
                    result = a ** 2

                elif choice == "9":
                    operation = f"{a} cubed"
                    result = a ** 3

                elif choice == "10":
                    if a < 0:
                        print("Error: Square root of a negative number "
                              "is not supported here.")
                        continue
                    operation = f"sqrt({a})"
                    result = math.sqrt(a)

                elif choice == "12":
                    if not a.is_integer() or a < 0:
                        print("Error: Factorial requires a "
                              "non-negative integer.")
                        continue
                    if a > 170:
                        print("Error: Number is too large for this "
                              "calculator's factorial display.")
                        continue
                    operation = f"{int(a)}!"
                    result = math.factorial(int(a))

                elif choice == "13":
                    operation = f"sin({a} degrees)"
                    result = math.sin(math.radians(a))

                elif choice == "14":
                    operation = f"cos({a} degrees)"
                    result = math.cos(math.radians(a))

                elif choice == "15":
                    if math.isclose(
                        math.cos(math.radians(a)), 0,
                        abs_tol=1e-12
                    ):
                        print("Error: Tangent is undefined at this angle.")
                        continue
                    operation = f"tan({a} degrees)"
                    result = math.tan(math.radians(a))

                elif choice == "16":
                    if a <= 0:
                        print("Error: Logarithm requires a positive number.")
                        continue
                    operation = f"log10({a})"
                    result = math.log10(a)

                else:
                    if a <= 0:
                        print("Error: Natural logarithm requires "
                              "a positive number.")
                        continue
                    operation = f"ln({a})"
                    result = math.log(a)

            elif choice == "11":
                value = get_number("Enter the total value: ")
                percent = get_number("Enter percentage: ")
                operation = f"{percent}% of {value}"
                result = (percent / 100) * value

            elif choice == "18":
                show_history()
                continue

            elif choice == "19":
                history.clear()
                print("Calculation history cleared.")
                continue

            else:
                print("Invalid choice! Please select 0-19.")
                continue

            if isinstance(result, complex) or not math.isfinite(result):
                print("Error: Result is outside the supported range.")
                continue

            print(f"\nResult: {result}")
            record_result(operation, result)

        except OverflowError:
            print("Error: The result is too large to calculate.")
        except ValueError as error:
            print(f"Calculation error: {error}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    calculate()
