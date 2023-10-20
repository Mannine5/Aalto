def sort_function(team):
    return(-team[1][7], -team[1][6], -team[1][4], team[1][0])


def make_league_table(file):

    league_table = {}

    for each in file:
        data = each.split(",")
        teams = data[1].strip().split("-")
        goals = data[0].split("-")

        team1_name = teams[0]
        team2_name = teams[1]

        # pl, w, d, l, f, a, gd, pts
        team1 = [1, 0, 0, 0, 0, 0, 0, 0]  # played game += 1
        team2 = [1, 0, 0, 0, 0, 0, 0, 0]  # played game += 1

        team1[4] = int(goals[0])  # goals for
        team1[5] = int(goals[1])  # goals against

        team2[4] = int(goals[1])  # goals for
        team2[5] = int(goals[0])  # goals against

        # print(team1_name, team1[4])
        # print(team2_name, team2[4])

        if (team1[4]) != (team2[4]):  # goals vs goals
            if (team1[4]) > (team2[4]):  # goals
                team1[1] = 1  # win
                team1[7] = 3  # points

                team2[3] = 1  # lose

            else:
                team2[1] = 1  # win
                team2[7] = 3  # points

                team1[3] = 1  # lose

        else:
            team1[2] = 1  # draw
            team1[7] = 1  # points

            team2[2] = 1  # draw
            team2[7] = 1  # draw

        team1[6] = (team1[4]) - (team1[5])  # goal difference
        team2[6] = (team2[4]) - (team2[5])  # goal difference

        if team1_name not in league_table:
            league_table[team1_name] = [0, 0, 0, 0, 0, 0, 0, 0]
        if team2_name not in league_table:
            league_table[team2_name] = [0, 0, 0, 0, 0, 0, 0, 0]

        new_teams1 = [0, 0, 0, 0, 0, 0, 0, 0]
        x = 0
        for team in league_table[team1_name]:
            new_teams1[x] = team + team1[x]
            x += 1
        league_table[team1_name] = new_teams1

        new_teams2 = [0, 0, 0, 0, 0, 0, 0, 0]
        y = 0
        for team in league_table[team2_name]:
            new_teams2[y] = team + team2[y]
            y += 1
        league_table[team2_name] = new_teams2

    return league_table


def print_league(sorted_league):

    print("Team                 Pl  W   D   L   F   A   GD  Pts")
    for each in sorted_league:
        line = f"{each[0]:20s}"
        for x in range(len(each[1])):
            line = line + f" {str(each[1][x]):<3s}"
        print(line)


def main():
    filename = input("Enter the name of the file used.\n")

    try:
        file = open(filename, "r")
        league = make_league_table(file)
        sorted_league = sorted(league.items(), key=sort_function)  # league is a dictionary
        print_league(sorted_league)

    except OSError:
        print("Error in reading the file. The program terminates.")


main()
