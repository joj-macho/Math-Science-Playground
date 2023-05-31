def main():
    '''Main function to get user input and compute GCD and LCM.'''

    print('\nGCD and LCM Calculator\n')

    while True:
        print('1. Compute GCD and LCM of two numbers')
        print('2. Quit Program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            compute_gcd_lcm()
        elif choice == '2':
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def compute_gcd_lcm():
    '''Function to compute GCD and LCM of two numbers.'''

    while True:
        try:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.')

    gcd = find_gcd(num1, num2)
    lcm = find_lcm(num1, num2)

    print(f'GCD of {num1} and {num2}: {gcd}\n')
    print(f'LCM of {num1} and {num2}: {lcm}\n')

def find_gcd(a, b):
    '''Returns the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.'''

    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    '''Returns the Least Common Multiple (LCM) of two numbers using GCD.'''

    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

if __name__ == '__main__':
    main()
