def sum_of_digits(n):
    """
    Calculates the sum of the digits of a number.
    """
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum


def is_magic_number(n):
    """
    Checks if a number is a magic number.
    """
    temp = n
    while len(str(temp)) > 1:
        temp = sum_of_digits(temp)
    return temp == 1


def main():
    """
    Main function to get user input and check if a number is a magic number.
    """
    print("Magic Number Checker\n")

    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if is_magic_number(number):
        print(f"{number} is a magic number.")
    else:
        print(f"{number} is not a magic number.")


if __name__ == "__main__":
    main()
