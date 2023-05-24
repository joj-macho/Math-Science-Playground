def is_kaprekar_number(number):
    """
    Checks if a number is a Kaprekar number.
    """
    square = number ** 2
    num_str = str(square)

    # Split the square into two parts
    for i in range(1, len(num_str)):
        left_part = int(num_str[:i])
        right_part = int(num_str[i:])

        # Check if the sum of the two parts is equal to the original number
        if left_part + right_part == number:
            return True

    return False


def main():
    """
    Main function to get user input and check if a number is a Kaprekar number.
    """
    print("Kaprekar Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_kaprekar_number(number):
        print(f"{number} is a Kaprekar number.")
    else:
        print(f"{number} is not a Kaprekar number.")


if __name__ == "__main__":
    main()
