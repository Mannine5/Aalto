import random

def make_key_list(file):

    countries_dictionary = {}

    for each in file:
        line = each.strip().split(",")
        if len(line) == 5:
            countries_dictionary[line[0]] = line[1] + "," + line[2] + "," + line[3] + "," + line [4]

    all_keys = countries_dictionary.keys()
    all_keys = list(countries_dictionary.keys())

    # all_keys = list(countries_dictionary)
    # What's the difference?? I don't get it.

    return all_keys, countries_dictionary

def play_a_game(keys_list, countries_dictionary):
    rounds = 3
    final_points = 0
    while rounds > 0:
        hint = 0
        random_country = random.choice(keys_list)
        country_info = countries_dictionary[random_country].split(",")
        print("Which country is this?")
        print("First hint:")
        quess = input(f"The capital city of this country: {country_info[hint]}.\n")

        while hint < 3:
            if quess != random_country:
                hint += 1
                if hint == 1:
                    print("Incorrect! Next hint:")
                    quess = input(f"The population of this country: {country_info[hint]}.\n")
                elif hint == 2:
                    print("Incorrect! Next hint:")
                    quess = input(f"The flag colors of this country: {country_info[hint]}.\n")
                elif hint == 3:
                    print("Incorrect! Next hint:")
                    quess = input(f"The continent of this country: {country_info[hint]}.\n")
                    if quess == random_country:
                        final_points = final_points + (4 - hint)
                        hint = 4
                        print("Correct!\n")
                    else:
                        hint = 4
                        print(f"Incorrect. The correct answer was {random_country}.\n")
            else:
                final_points = final_points + (4 - hint)
                hint = 4
                print("Correct!\n")

        keys_list.remove(random_country)
        rounds -= 1

    print(f"Game finished. You got {final_points} points.")

def main ():

    filename = input("Enter a filename:\n")

    #Initialize random module
    seed_number = int(input("Enter a seed:\n"))
    random.seed(seed_number)

    try:
        file = open(filename, "r")
        keys_list, countries_dictionary = make_key_list(file)
        play_a_game(keys_list,countries_dictionary)

    except OSError:
        print("Error in reading the file unknown.txt. Closing program.")


main()