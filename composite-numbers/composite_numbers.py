def is_composite(n):
    """
    Checks if a number is composite.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False


def main():
    """
    Main function to get user input and check if a number is composite.
    """
    print("Composite Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_composite(number):
        print(number, "is a composite number.")
    else:
        print(number, "is not a composite number.")


if __name__ == "__main__":
    main()
