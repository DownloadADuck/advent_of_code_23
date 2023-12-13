from functools import reduce
import operator

def game_power_calc(game_rounds):
    cube_count = { 'red': 0, 'green': 0, 'blue': 0 }

    for round_data in game_rounds:
        round_data = round_data.strip().split(', ')
        for cube in round_data:
            quantity, color = cube.split()
            cube_count[color] += int(quantity)
    print("cube_count", cube_count)
    print("game_power", reduce(operator.mul, cube_count.values(), 1))
    return reduce(operator.mul, cube_count.values(), 1)

def main():
    with open('test.txt', 'r') as file:
        lines = file.readlines()

    total_cubes = { 'red': 12, 'green': 13, 'blue': 14 }
    possible_games = []

    for idx, line in enumerate(lines):
        game_data = line.split(':')
        game_id = game_data[0].strip()
        game_rounds = game_data[1].split(';')

        print("game_id", game_id)
        game_power = game_power_calc(game_rounds)

        #if is_game_possible(game_rounds, total_cubes):
        #    print("possible!")
        #    possible_games.append(int(game_id.split()[1]))

    result = sum(possible_games)
    print("Possible games: ", possible_games)
    print("Result --> ", result)

if __name__ == "__main__":
    main()
