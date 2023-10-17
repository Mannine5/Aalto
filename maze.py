import random

SIZE = 8
PLAYER_POSITION = [1, 1]
EXIT_POSITION = [SIZE, SIZE]

def add_random_treasures(maze):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if maze[i][j] == '   ' or maze[i][j] == ' * ':
                if random.choice([True, False]) == True:
                    maze[i][j] = f" {random.randint(1, 5)} "
    return maze

def add_random_paths(maze):
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if random.choice([True, False]) == True:
                maze[i][j] = '   '
    return maze


# Implement the missing functions here
def init_maze(maze):
    for i in range(SIZE + 2):
        row = [""] * (SIZE + 2)
        for j in range(SIZE + 2):
            row[j] = " * "
        maze.append(row)
    return maze


def create_paths(maze):
    for i in range(len(maze)):
        if i != 0 and i != len(maze) - 1:
            maze[i][1] = "   "
            maze[i][len(maze[i]) - 2] = "   "
        if i == 1 or i == len(maze) - 2:
            for j in range(1, len(maze[0]) - 1):
                maze[i][j] = "   "
    return maze


def print_maze2(maze, player_position):
    maze[len(maze) - 2][len(maze[0]) - 2] = " E "
    for i in range(SIZE + 2):
        row = ""
        for j in range(SIZE + 2):
            if " P " != player_position[i][j]:
                row += (maze[i][j])
            else:
                row += (player_position[i][j])
        print(row)


def generate_maze(maze):
    init_maze(maze)
    create_paths(maze)
    add_random_treasures(maze)
    add_random_paths(maze)
    return maze


def init_position(player_position):
    for i in range(SIZE + 2):
        row = [""] * (SIZE + 2)
        for j in range(SIZE + 2):
            row[j] = ""
        player_position.append(row)
    player_position[1][1] = " P "
    return player_position


def player_movements(maze, player_position):

    player_score = 0

    finish = False
    i = 1
    j = 1
    while not finish:
        print_maze2(maze, player_position)
        #print(player_score)
        move = input("Enter your move (W/A/S/D):\n").upper()

        if move == "W":
            i -= 1
            if maze[i][j] == " * ":
                i += 1
                if maze[i][j] != "   " and 0 < int(maze[i][j]):
                    player_score += int(maze[i][j])
                    maze[i][j] = "   "
            elif maze[i][j] == " E ":
                player_score -= 1
                finish = True
            elif maze[i][j] == "   ":
                player_score -= 1
                player_position[i + 1][j] = ""
                player_position[i][j] = " P "
            elif int(maze[i][j]) > 0:
                player_score -= 1
                player_score += int(maze[i][j])
                maze[i][j] = "   "
                player_position[i + 1][j] = ""
                player_position[i][j] = " P "

        if move == "A":
            j -= 1
            if maze[i][j] == " * ":
                j += 1
                if maze[i][j] != "   " and 0 < int(maze[i][j]):
                    player_score += int(maze[i][j])
                    maze[i][j] = "   "
            elif maze[i][j] == " E ":
                player_score -= 1
                finish = True
            elif maze[i][j] == "   ":
                player_score -= 1
                player_position[i][j + 1] = ""
                player_position[i][j] = " P "
            elif int(maze[i][j]) > 0:
                player_score -= 1
                player_score += int(maze[i][j])
                maze[i][j] = "   "
                player_position[i][j + 1] = ""
                player_position[i][j] = " P "

        if move == "S":
            i += 1
            if maze[i][j] == " * ":
                i -= 1
                if maze[i][j] != "   " and 0 < int(maze[i][j]):
                    player_score += int(maze[i][j])
                    maze[i][j] = "   "
            elif maze[i][j] == " E ":
                player_score -= 1
                finish = True
            elif maze[i][j] == "   ":
                player_score -= 1
                player_position[i - 1][j] = ""
                player_position[i][j] = " P "
            elif int(maze[i][j]) > 0:
                player_score -= 1
                player_score += int(maze[i][j])
                maze[i][j] = "   "
                player_position[i - 1][j] = ""
                player_position[i][j] = " P "

        if move == "D":
            j += 1
            if maze[i][j] == " * ":
                j -= 1
                if maze[i][j] != "   " and 0 < int(maze[i][j]):
                    player_score += int(maze[i][j])
                    maze[i][j] = "   "
            elif maze[i][j] == " E ":
                player_score -= 1
                finish = True
            elif maze[i][j] == "   ":
                player_score -= 1
                player_position[i][j - 1] = ""
                player_position[i][j] = " P "
            elif int(maze[i][j]) > 0:
                player_score -= 1
                player_score += int(maze[i][j])
                maze[i][j] = "   "
                player_position[i][j - 1] = ""
                player_position[i][j] = " P "
        if finish:
            print("Congratulations, you've escaped the maze with", player_score, "points!")


def main():
    seed_number = input("Enter a seed:\n")
    random.seed(seed_number)
    maze = []

    # Continue writing the main function here
    player_position = []
    init_position(player_position)
    generate_maze(maze)
    player_movements(maze, player_position)


main()
