def is_perfect_number(number):
    """
    Check if a given number is a perfect number.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - bool: True if the number is a perfect number, False otherwise.
    """
    divisors = [1]  # Initialize with 1 as a divisor
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)

    return sum(divisors) == number


def main():
    """
    This program checks if a given number is a perfect number.
    """
    print("Perfect Number Checker\n")

    # Get input from the user
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number > 0:
                break
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Check if the number is a perfect number
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")


# Execute the main function
if __name__ == "__main__":
    main()
