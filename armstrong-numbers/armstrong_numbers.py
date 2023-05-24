def is_armstrong_number(number):
    """
    Checks if a number is an Armstrong number.
    """
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    return number == armstrong_sum


def main():
    """
    Main function to get user input and check if a number is an Armstrong number.
    """
    print("Armstrong Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")


if __name__ == "__main__":
    main()
