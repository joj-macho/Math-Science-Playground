def is_harshad_number(n):
    """
    Checks if a number is a Harshad number.
    """
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0


def main():
    """
    Main function to get user input and check if a number is a Harshad number.
    """
    print("Harshad Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_harshad_number(number):
        print(f"{number} is a Harshad number.")
    else:
        print(f"{number} is not a Harshad number.")


if __name__ == "__main__":
    main()
