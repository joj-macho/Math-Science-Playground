def calculate_gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    Parameters:
    - a (int): First number
    - b (int): Second number

    Returns:
    - int: GCD of the two numbers
    """
    while b:
        a, b = b, a % b
    return a


def calculate_lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers.

    Parameters:
    - a (int): First number
    - b (int): Second number

    Returns:
    - int: LCM of the two numbers
    """
    gcd_result = calculate_gcd(a, b)
    if gcd_result == 0:
        return 0
    return (a * b) // gcd_result


def main():
    """
    This program calculates the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers.
    """
    print("GCD and LCM Calculator\n")

    # Get input from the user
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if num1 > 0 and num2 > 0:
                break
            else:
                print("Invalid input. Please enter positive integers.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Calculate GCD and LCM
    gcd_result = calculate_gcd(num1, num2)
    lcm_result = calculate_lcm(num1, num2)

    # Display the results
    print(f"The GCD of {num1} and {num2} is: {gcd_result}")
    print(f"The LCM of {num1} and {num2} is: {lcm_result}")


# Execute the main function
if __name__ == "__main__":
    main()
