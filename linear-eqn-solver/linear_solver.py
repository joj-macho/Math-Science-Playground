def main():
    '''Main function for finding the root of a linear equation.'''

    print('\nLinear Equation Solver\n')

    while True:
        try:
            a = float(input('Enter a: '))
            b = float(input('Enter b: '))
            break
        except ValueError:
            print('Invalid input. Please enter numeric values for a and b')

    result = linear_equation_solver(a, b)
    print()
    print(result)


def linear_equation_solver(a, b):
    '''Solves a linear equation ax + b = 0.'''
    
    if a == 0:
        if b == 0:
            return 'Infinite solutions (identity equation)'
        else:
            return 'No solution (contradictory equation)'
    else:
        x = -b / a
        return f'Solution: x = {x}'


if __name__ == '__main__':
    main()