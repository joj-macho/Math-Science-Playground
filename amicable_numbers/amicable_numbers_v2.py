def get_divisors(n):
    """
    Returns a list of divisors of a given number.
    """
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def is_amicable(a, b):
    """
    Checks if two numbers are amicable numbers.
    """
    divisors_a = get_divisors(a)
    sum_a = sum(divisors_a) - a

    divisors_b = get_divisors(b)
    sum_b = sum(divisors_b) - b

    return sum_a == b and sum_b == a


def find_amicable_pairs(start, end):
    """
    Finds and prints all amicable number pairs within a given range.
    """
    amicable_pairs = []
    for i in range(start, end + 1):
        sum_divisors = sum(get_divisors(i)) - i
        if sum_divisors > i and is_amicable(i, sum_divisors):
            amicable_pairs.append((i, sum_divisors))

    if amicable_pairs:
        print("Amicable number pairs within the range:")
        for pair in amicable_pairs:
            print(pair[0], "and", pair[1])
    else:
        print("No amicable number pairs found within the range.")


def main():
    """
    Main function to get user input and find amicable number pairs.
    """
    print("Amicable Number Finder\n")

    while True:
        try:
            start = int(input("Enter the starting number: "))
            end = int(input("Enter the ending number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    find_amicable_pairs(start, end)


if __name__ == "__main__":
    main()
