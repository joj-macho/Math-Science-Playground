def is_perfect_square(number):
    """
    Checks if a number is a perfect square.
    """
    if number < 0:
        return False

    root = int(number ** 0.5)
    return root * root == number


def main():
    """
    Main function to get user input and check if a number is a perfect square.
    """
    print("Perfect Square Check\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if is_perfect_square(number):
        print(f"{number} is a perfect square.")
    else:
        print(f"{number} is not a perfect square.")


if __name__ == "__main__":
    main()
