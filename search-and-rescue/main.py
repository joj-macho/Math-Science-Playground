from search import SearchAndRescueMission

def main():
    # Instantiate the SearchAndRescueMission class
    mission = SearchAndRescueMission()

    # Choose the hiker's location
    mission.hiker_final_location()

    # Print initial target probabilities (priors)
    print('Initial Target Probabilities:')
    for area in mission.pre_search_probabilities:
        print(f'{area}: {mission.pre_search_probabilities[area]} |', end=' ')
    print()

    searches_conducted = 0

    # Run the simulation
    while True:
        print('\nChoose the area to search:')
        print('1 - Search Area 1')
        print('2 - Search Area 2')
        print('3 - Search Area 3')
        print('0 - Quit')
        print()
        
        # Get user choice
        choice = input('Enter your choice: ')

        if choice == '0':
            print(f'\nSimulation ended. Total searches conducted: {searches_conducted}')
            break

        elif choice in ['1', '2', '3']:
            # Calculate search effectiveness values for each search area
            mission.calculate_search_effectiveness()

            area_number = f'Area {choice}'
            area_coordinates = getattr(mission, f'search_area_{choice}')
            search_effectiveness = mission.search_effort_probabilities[area_number]

            # Display the map before conducting a search
            mission.draw_map()

            results, searched_coords = mission.conduct_search(area_number, area_coordinates, search_effectiveness)

            # Update probabilities based on the search result
            mission.update_probabilities(area_number, results)

            # Display search results
            print('\nSearch Results:')
            if results == 'Not Found':
                print(f'Hiker not found in {area_number}')
                
                # Display updated probabilities
                print('\nUpdated Target Probabilities:')
                for area, prob in mission.pre_search_probabilities.items():
                    print(f'{area}: {prob:.3f} |', end=' ')
                print()

            else:
                # Draw the map with the hiker's found location marked
                print('Map with hiker location')
                mission.draw_map()
                print()

                print(f'Hiker found at {searched_coords} in {area_number}.')
            
            print(f'Search Effectiveness: {search_effectiveness:.3f}')

            searches_conducted += 1
            print()
            print('-'*42)

        else:
            print('\nSorry, but that isn\'t a valid choice.')

if __name__ == '__main__':
    main()