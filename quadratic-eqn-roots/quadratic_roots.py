import math
import cmath  # complex math library

def main():
    '''Main function for finding the roots of a quadratic equation.'''
    
    print('\nQuadratic Equation Solver\n')

    while True:
        try:
            a = float(input('Enter a: '))
            if a == 0:
                print('a must be a non-zero value.')
                continue
            b = float(input('Enter b: '))
            c = float(input('Enter c: '))
            break
        except ValueError:
            print('Invalid input. Please enter numeric values for a, b, and c.')

    # Calculate roots
    roots = calculate_roots(a, b, c)

    # Results
    if roots:
        if len(roots) == 1:
            print(f'\nOne real root (repeated):\nRoot: {roots[0]}')
        else:
            root1, root2 = roots
            print(f'\nTwo roots (real or complex):\nRoot 1: {root1}\nRoot 2: {root2}')
    else:
        print('No real roots')
        

def calculate_roots(a, b, c):
    '''Calculate the roots of the quadratic equation, including complex roots.'''
    
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Calculate two real roots
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        # Calculate one real root (repeated)
        x1 = -b / (2 * a)
        return x1,
    else:
        # Use complex numbers to handle imaginary roots
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    main()
