
def main():
    '''Main function to get the number of rows and display Pascal's Triangle.'''

    print("\nPascal's Triangle\n")

    while True:
        try:
            rows = int(input('Enter the number of rows:\n> '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    display_pascals_triangle(rows)

def display_pascals_triangle(rows):
    '''Function to display Pascal's Triangle.'''

    for i in range(rows):
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=' ')
        print()

def binomial_coefficient(n, k):
    '''Function to calculate the binomial coefficient.'''

    return factorial(n) // (factorial(k) * factorial(n - k))

def factorial(n):
    '''Function to calculate factorial.'''

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    main()
