import math

def is_perfect_number(number):
    """
    Check if a given number is a perfect number.

    Parameters:
    - number (int): The number to be checked.

    Returns:
    - bool: True if the number is a perfect number, False otherwise.
    """
    if number <= 0:
        return False

    divisor_sum = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:  # Avoid adding the square root twice
                divisor_sum += number // i

    return divisor_sum == number


def main():
    """
    This program checks if a given number is a perfect number.
    """
    print("Perfect Number Checker\n")

    # Get input from the user
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            break
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
