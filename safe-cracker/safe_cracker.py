import time
from random import randint, randrange
from itertools import product


def main():
    '''Main function to run the program.'''

    print('\nSafe Cracker.\n')

    combination = input('Enter the lock combination to crack:\n> ')
    start_time = time.time()

    hill_climbing_cracker(combination)
    # brute_force_cracker(combination)  # Uncomment this line to use brute force method

    end_time = time.time()
    duration = end_time - start_time
    print('\nRuntime for this program was {:.5f} seconds.'.format(duration))


def fitness(combo, attempt):
    '''Compare items in two lists and count number of matches.'''
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade

def hill_climbing_cracker(combination):
    '''Use hill climbing to crack a lock combination.'''

    print('Cracking Combination: {}'.format(combination))
    combo = [int(i) for i in combination]

    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    while best_attempt != combo:
        next_try = best_attempt[:]
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        count += 1

    print('Combination Cracked! {}'.format(best_attempt))
    print('Cracked in {} tries.'.format(count))

def brute_force_cracker(combination):
    '''Use brute force to crack a lock combination.'''

    print('Cracking Combination: {}'.format(combination))

    for perm in product(range(10), repeat=len(combination)):
        if perm == combination:
            print('Combination Cracked!')
            print('Cracked Result: {}'.format(perm))
            break


if __name__ == '__main__':
    main()
