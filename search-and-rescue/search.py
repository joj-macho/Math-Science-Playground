import random

# Search area corner point locations
AREA_1_RECT = (6, 0, 25, 9)
AREA_2_RECT = (12, 10, 31, 19)
AREA_3_RECT = (32, 4, 51, 13)


class SearchAndRescueMission:
    def __init__(self):
        # Create a new 60x20 map data structure.
        self.map = self.generate_new_map()

        # Pre-search probabilities for finding the hiker in each search area
        self.pre_search_probabilities = {'Area 1': 0.2, 'Area 2': 0.3, 'Area 3': 0.5}

        # Initialize search effort probabilities (SEP)
        self.search_effort_probabilities = {'Area 1': 0.0, 'Area 2': 0.0, 'Area 3': 0.0}

        # Initialize hiker's actual location when found
        self.hiker_found_area = None
        self.hiker_found_coordinates = None

        # Initialize searched coordinates
        self.searched_coordinates = set()

        # Local coordinates within each area
        self.search_area_1 = [(i, j) for i in range(AREA_1_RECT[0]+1, AREA_1_RECT[2]) for j in range(AREA_1_RECT[1]+1, AREA_1_RECT[3])]
        self.search_area_2 = [(i, j) for i in range(AREA_2_RECT[0]+1, AREA_2_RECT[2]) for j in range(AREA_2_RECT[1]+1, AREA_2_RECT[3])]
        self.search_area_3 = [(i, j) for i in range(AREA_3_RECT[0]+1, AREA_3_RECT[2]) for j in range(AREA_3_RECT[1]+1, AREA_3_RECT[3])]

        # Display the initial map
        self.draw_map()

    def hiker_final_location(self):
        # Choose a random search area
        chosen_area = random.choice(['Area 1', 'Area 2', 'Area 3'])

        # Set the chosen area as the hiker's found area
        self.hiker_found_area = chosen_area

        # Choose a random location within the selected search area
        if chosen_area == 'Area 1':
            self.hiker_found_coordinates = random.choice(self.search_area_1)
        elif chosen_area == 'Area 2':
            self.hiker_found_coordinates = random.choice(self.search_area_2)
        elif chosen_area == 'Area 3':
            self.hiker_found_coordinates = random.choice(self.search_area_3)

    def calculate_search_effectiveness(self):
        # Calculate search effectiveness values for each search area
        for area in self.search_effort_probabilities:
            self.search_effort_probabilities[area] = random.uniform(0.2, 0.9)

    def conduct_search(self, area_number, area_coordinates, search_effectiveness):
        # Display the map before each search
        self.draw_map()

        # Exclude previously searched coordinates
        search_coordinates = list(set(area_coordinates) - self.searched_coordinates)

        # Sample the coordinates based on search effectiveness
        random.shuffle(search_coordinates)
        search_coordinates = search_coordinates[:int(len(search_coordinates) * search_effectiveness)]

        # Mark searched coordinates on the map with 'O'
        for x, y in search_coordinates:
            self.map[x][y] = 'O'

        # Check if the hiker is found in the searched locations
        hiker_actual_coordinates = self.hiker_found_coordinates
        if hiker_actual_coordinates in search_coordinates:
            return 'Found in ' + area_number, hiker_actual_coordinates
        return 'Not Found', area_number

    def update_probabilities(self, search_area, search_result):
        # Bayesian update of probabilities based on search effectiveness
        prior_probabilities = self.pre_search_probabilities.copy()
        search_efficiencies = self.search_effort_probabilities.copy()

        # Calculate the likelihood for all search areas
        likelihoods = {}
        for area in prior_probabilities:
            if search_result == 'Found in ' + area:
                likelihoods[area] = search_efficiencies[area]
            else:
                likelihoods[area] = 1 - search_efficiencies[area]

        # Calculate the evidence for all search areas
        evidence = sum([
            prior_probabilities[area] * (1 - search_efficiencies[area])
            for area in prior_probabilities
        ])

        # Update the probability for all search areas using Bayes' theorem
        for area in self.pre_search_probabilities:
            self.pre_search_probabilities[area] = (prior_probabilities[area] * likelihoods[area]) / evidence

    def generate_new_map(self):
        # Create a new 60x20 map data structure.
        return [[' ' for _ in range(21)] for _ in range(60)]

    def draw_map(self):
        # Draw the map data structure.
        grid_num_line = '    '  # Initial space for the numbers down the top_x side of the map
        for i in range(1, 6):
            grid_num_line += (' ' * 9) + str(i)

        # Print the numbers across the top_y of the map.
        print(grid_num_line)
        print('   ' + ('0123456789' * 6))
        print()

        # Draw Search Areas
        self.draw_search_area(*AREA_1_RECT, 'Area 1')
        self.draw_search_area(*AREA_2_RECT, 'Area 2')
        self.draw_search_area(*AREA_3_RECT, 'Area 3')

        # Mark the hiker's found location on the map
        if self.hiker_found_coordinates:
            hiker_x, hiker_y = self.hiker_found_coordinates
            self.map[hiker_x][hiker_y] = 'X'

        # Print each of the 21 rows.
        for row in range(21):
            # Single-digit numbers need to be padded with an extra space.
            extra_space = ' ' if row < 10 else ''

            # Create the string for this row on the map.
            map_row = ''.join(self.map[column][row] for column in range(60))

            print('%s%s %s %s' % (extra_space, row, map_row, row))

        # Print the numbers across the bottom_y of the map.
        print()
        print('   ' + ('0123456789' * 6))
        print(grid_num_line)

    def draw_search_area(self, top_x, top_y, bottom_x, bottom_y, label):
        for i in range(top_y, bottom_y + 1):
            for j in range(top_x, bottom_x + 1):
                if i == top_y or i == bottom_y:
                    if j == top_x:
                        self.map[j][i] = '+'
                    elif j == bottom_x:
                        self.map[j][i] = '+'
                    else:
                        self.map[j][i] = '-'
                elif j == top_x or j == bottom_x:
                    self.map[j][i] = '|'
                elif i == top_y + 1 and top_x + 2 <= j <= top_x + 2 + len(label) - 1:
                    self.map[j][i] = label[j - (top_x + 2)]

