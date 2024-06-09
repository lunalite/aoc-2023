document = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

example = document.split('\n')

sum_of_power = 0
for i in example:
    game, records = i.split(':')
    game_id = game.split(' ')[1]

    max_red = 0
    max_blue = 0
    max_green = 0

    for record in records.split(';'):
        for cube in record.split(','):
            split = cube.split(' ')
            num_of_cubes = int(split[1])
            color = split[2]
            if color == 'blue':
                if num_of_cubes > max_blue:
                    max_blue = num_of_cubes
            elif color == 'red':
                if num_of_cubes > max_red:
                    max_red = num_of_cubes
            elif color == 'green':
                if num_of_cubes > max_green:
                    max_green = num_of_cubes
    power = max_blue * max_green * max_red
    sum_of_power += power
print(sum_of_power)
