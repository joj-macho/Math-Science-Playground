import datetime
import random
import sys


def main():
    '''
    Main function to run the birthday paradox simulation.
    '''
    print('''
The Birthday Paradox!
In a set of n-randomly selected people, what is the probability that at least two people share the same birthday? What is the smallest value of n where the probability is at least 50% or 99%?

This program performs multiple simulations to determine the percentage of people sharing the same birthday for various group sizes.
    ''')

    # Prompt the user to enter a valid number of birthdays
    while True:
        response = input('How many birthdays (max = 100) do you want to generate?\nEnter (q)uit to exit the program.\n> ')
        if response.lower() == 'q':
            print('Bye!')
            sys.exit()
        if response.isdecimal() and 0 < int(response) <= 100:
            number_of_birthdays = int(response)
            break

    birthdays = generate_birthdays(number_of_birthdays)
    display_birthdays(birthdays)

    birthday_match = find_birthday_match(birthdays)
    print(f'In this group of {number_of_birthdays} people ...', end=' ')
    if birthday_match:
        birth_month = birthday_match.strftime("%B")
        birth_date = f"{birthday_match.day} {birth_month}"
        print(f"Multiple people share the birthday {birth_date}\n")
    else:
        print("No people share the same birthday!\n")

    num_simulations = 100_000
    print(f"Performing {num_simulations} simulations with {number_of_birthdays} birthdays...")
    probability, matches = perform_simulations(number_of_birthdays, num_simulations)
    print(
        f"\nIn the {num_simulations} simulations of {number_of_birthdays} people/birthdays:\n"
        f"There are {matches} matching birthdays in the group after {num_simulations} simulations.\n"
        f"That is, {number_of_birthdays} people have a {probability:.3f}% chance of having the same birthday in their group."
    )


def generate_birthdays(number_of_birthdays):
    '''This function generates a list of random birthdays for the specified number of people.'''

    birthdays = []
    for _ in range(number_of_birthdays):
        year_start = datetime.date(1990, 1, 1)
        num_of_days = datetime.timedelta(random.randint(0, 364))
        random_date = year_start + num_of_days
        birthdays.append(random_date)
    return birthdays


def display_birthdays(birthdays):
    '''This function displays the list of birthdays.'''

    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(f'\n{len(birthdays)} Birthdays Randomly Generated:')
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        birth_month = MONTHS[birthday.month - 1]
        birth_date = f'{birthday.day} {birth_month}'
        print(birth_date, end='')
    print('\n')


def find_birthday_match(birthdays):
    '''This function checks if any birthdays in the list occur more than once and return the first matching birthday found.'''

    if len(birthdays) == len(set(birthdays)):
        return None
    for i, birthday_i in enumerate(birthdays):
        for birthday_j in birthdays[i + 1:]:
            if birthday_i == birthday_j:
                return birthday_i


def perform_simulations(number_of_birthdays, num_simulations):
    '''This function performs simulations to determine the percentage of people sharing the same birthday for the given group size.'''

    matches = 0
    for i in range(num_simulations):
        if i % 10_000 == 0:
            print(f'{i} Simulations Completed...')
        birthdays = generate_birthdays(number_of_birthdays)
        if find_birthday_match(birthdays) is not None:
            matches += 1
    probability = (matches / num_simulations) * 100
    return probability, matches




if __name__ == '__main__':
    main()
