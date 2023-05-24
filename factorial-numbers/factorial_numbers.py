def factorial(n):
    """
    Calculates the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    """
    Main function to get user input and calculate the factorial.
    """
    print("Factorial Calculator\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")


if __name__ == "__main__":
    main()
