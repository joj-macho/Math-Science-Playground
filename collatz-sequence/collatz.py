import sys
import time


def main():
    '''This is the main function that runs the Collatz Sequence program.'''
    
    print('\nThe Collatz Sequence.\n')
    
    # Enter a valid integer value.
    while True:
        response = input(
            'Enter a number greater than 0 or (q)uit to exit.\n> ').lower()

        if response.startswith('q'):
            print('Bye!')
            sys.exit()
        
        try:
            number = int(response)
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print('Enter a valid positive integer.')
    
    print(f'\nCollatz Sequence starting from {number}:')
    print(number, end='', flush=True)
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        print(f', {number}', end='', flush=True)

        time.sleep(0.1)

    print()


if __name__ == '__main__':
    main()
