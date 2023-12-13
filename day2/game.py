def is_game_possible(game_rounds, total_cubes):
    total_cubes_copy = total_cubes.copy()

    for round_data in game_rounds:
        current_cubes = total_cubes_copy.copy()
        round_data = round_data.strip().split(', ')
        for cube in round_data:
            quantity, color = cube.split()
            current_cubes[color] -= int(quantity)
            print("current_cubes", current_cubes[color], color)
            if current_cubes[color] < 0:
                print("current_cubes[color]", current_cubes, color)
                return False

        #total_cubes_copy = current_cubes.copy()

    return True

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    total_cubes = { 'red': 12, 'green': 13, 'blue': 14 }
    possible_games = []

    for idx, line in enumerate(lines):
        game_data = line.split(':')
        game_id = game_data[0].strip()
        game_rounds = game_data[1].split(';')

        print("game_id", game_id)
        if is_game_possible(game_rounds, total_cubes):
            print("possible!")
            possible_games.append(int(game_id.split()[1]))

    result = sum(possible_games)
    print("Possible games: ", possible_games)
    print("Result --> ", result)

if __name__ == "__main__":
    main()
