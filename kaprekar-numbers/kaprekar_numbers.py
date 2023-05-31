
def main():
    '''Main function to check Kaprekar numbers.'''

    print('\nKaprekar Number Checker\n')

    while True:
        print('1. Check if a number is Kaprekar')
        print('2. List Kaprekar numbers within a range')
        print('3. Enter (q)uit to exit program')

        choice = input('Enter your choice:\n> ')

        if choice == '1':
            check_kaprekar_number()
        elif choice == '2':
            list_kaprekar_numbers()
        elif choice == '3' or choice.startswith('q'):
            print('Bye.')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

def check_kaprekar_number():
    '''Function to check if a number is Kaprekar.'''

    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.\n')

    if is_kaprekar(number):
        print(f'{number} is a Kaprekar number.\n')
    else:
        print(f'{number} is not a Kaprekar number.\n')

def list_kaprekar_numbers():
    '''Function to list Kaprekar numbers within a range.'''

    while True:
        try:
            start = int(input('Enter the starting number: '))
            end = int(input('Enter the ending number: '))
            break
        except ValueError:
            print('Invalid input. Please enter valid integers.\n')

    if start > end:
        print('Invalid range. Starting number should be less than or equal to the ending number.\n')
        return

    kaprekar_numbers = []
    for number in range(start, end + 1):
        if is_kaprekar(number):
            kaprekar_numbers.append(number)

    if kaprekar_numbers:
        print('Kaprekar numbers within the range:', kaprekar_numbers)
    else:
        print('No Kaprekar numbers within the range.\n')

def is_kaprekar(n):
    '''Checks if a number is Kaprekar.'''

    square = n**2
    digits = len(str(square))
    
    for i in range(1, digits):
        divisor = 10**i
        if divisor == n:
            continue
        
        sum_parts = square // divisor + square % divisor
        if sum_parts == n:
            return True
    
    return False

if __name__ == '__main__':
    main()
