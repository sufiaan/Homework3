"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 11.27
"""

import collections

player_dict = {}

for i in range(1, 6):
    jersey_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()

    player_dict[jersey_number] = rating
    sorted_dict = collections.OrderedDict(sorted(player_dict.items()))

print('ROSTER')
for keys, values in sorted_dict.items():
    print('Jersey number:', str(keys) + ',', 'Rating:', values)

option = ''
while option.upper() != 'Q':
    print("\nMENU\n" "a - Add player\n" "d - Remove player\n" "u - Update player rating\n" 
          "r - Output players above a rating\n" "o - Output roster\n" "q - Quit\n")
    option = input('Choose an option:\n')

    if option == 'a':
        new_number = int(input('Enter a new player\'s jersey number:\n'))
        new_rating = int(input('Enter the player\'s rating:\n'))
        sorted_dict.update({new_number: new_rating})

    elif option == 'd':
        remove_player = int(input('Enter a jersey number:\n'))
        sorted_dict.pop(remove_player)

    elif option == 'u':
        update_num = int(input('Enter a jersey number:\n'))
        update_rating = int(input('Enter a new rating for player:\n'))
        sorted_dict[update_num] = update_rating

    elif option == 'r':
        above_rating = int(input('Enter a rating:\n'))
        new_dict = {}
        for num, rating in sorted_dict.items():
            if rating > above_rating:
              new_dict.update({num: rating})
            print("ABOVE " + str(above_rating))

            for key, value in new_dict.items():
              print('Jersey number:', str(key) + ',', 'Rating:', value)

    elif option == 'o':
        print('ROSTER')
        sorted_dict = collections.OrderedDict(sorted(sorted_dict.items()))
        for num, rating in sorted_dict.items():
            print('Jersey number:', str(num) + ',', 'Rating:', rating)