def sum_of_proper_divisors(number):
    """
    Calculate the sum of proper divisors of a given number.

    Parameters:
    - number (int): The number for which to calculate the sum of proper divisors.

    Returns:
    - int: The sum of proper divisors.
    """
    divisors_sum = 1  # Initialize sum with 1 since every number is divisible by 1

    # Iterate from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Add the pair divisor only if it is distinct
                divisors_sum += number // i

    return divisors_sum


def find_amicable_numbers(start, end):
    """
    Find pairs of amicable numbers within a given range.

    Parameters:
    - start (int): The starting number of the range.
    - end (int): The ending number of the range.

    Returns:
    - list: A list of tuples containing pairs of amicable numbers.
    """
    amicable_pairs = []

    # Iterate over the range of numbers
    for number in range(start, end + 1):
        sum1 = sum_of_proper_divisors(number)

        # Check if the sum of proper divisors is different from the number itself
        if sum1 != number:
            sum2 = sum_of_proper_divisors(sum1)

            # Check if the second sum of proper divisors is equal to the original number
            if sum2 == number:
                amicable_pairs.append((number, sum1))

    return amicable_pairs


def main():
    """
    This program finds pairs of amicable numbers within a given range.
    """
    print("Amicable Numbers\n")

    # Get input from the user
    while True:
        try:
            start = int(input("Enter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))
            if start <= end:
                break
            else:
                print("Invalid input. The starting number should be less than or equal to the ending number.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Find amicable numbers
    amicable_pairs = find_amicable_numbers(start, end)

    # Display the amicable pairs
    if amicable_pairs:
        print("The amicable pairs within the given range are:")
        for pair in amicable_pairs:
            print(pair)
    else:
        print("No amicable pairs found within the given range.")

# Execute the main function
if __name__ == "__main__":
    main()
