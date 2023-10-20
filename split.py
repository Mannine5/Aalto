def main():
    league = ["0-0, Manchester United-Chelsea",
              "0-1, Chelsea-Liverpool", "1-3, Liverpool-Manchester United"]

    league_table = {}


    for each in league:
        data = each.split(",")
        teams = data[1].strip().split("-")
        goals = data[0].split("-")

        team1_name = teams[0]
        team2_name = teams[1]

        # pl, w, d, l, f, a, gd, pts
        team1 = [1, 0, 0, 0, 0, 0, 0, 0] # played game += 1
        team2= [1, 0, 0, 0, 0, 0, 0, 0] # played game += 1

        team1[4] = int(goals[0]) # goals for
        team1[5] = int(goals[1]) # goals against

        team2[4] = int(goals[1]) # goals for
        team2[5] = int(goals[0]) # goals against

        #print(team1_name, team1[4])
       # print(team2_name, team2[4])

        if int(team1[4]) != int(team2[4]): # goals vs goals
            if int(team1[4]) > int(team2[4]): # goals
                team1[1] = 1 # win
                team1[7] = 3 # points

                team2[3] = 1 # lose

            else:
                team2[1] = 1 # win
                team2[7] = 3 # points

                team1[3] = 1 # lose

        else:
            team1[2] = 1 # draw
            team1[7] = 1 # points

            team2[2] = 1 # draw
            team2[7] = 1 # draw

        team1[6] = int(team1[4]) - int(team1[5]) # goal difference
        team2[6] = int(team2[4]) - int(team2[5]) # goal difference


        if team1_name not in league_table:
            league_table[team1_name] = [0, 0, 0, 0, 0, 0, 0, 0]
        if team2_name not in league_table:
            league_table[team2_name] = [0, 0, 0, 0, 0, 0, 0, 0]

        new_teams1 = [0, 0, 0, 0, 0, 0, 0, 0]
        x = 0
        for each in league_table[team1_name]:
            new_teams1[x] = each + team1[x]
            x += 1
        league_table[team1_name] = new_teams1

        new_teams2 = [0, 0, 0, 0, 0, 0, 0, 0]
        y = 0
        for each in league_table[team2_name]:
            new_teams2[y] = each + team2[y]
            y += 1
        league_table[team2_name] = new_teams2


    print(league_table)


main()

{Pl:<3s} {W:<3s} {D:<3s} {L:<3s} {F:<3s} {A:<3s} {GD:<3s} {Pts:<3s}")