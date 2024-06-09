document = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

example = document.split('\n')

max_red = 12
max_green = 13
max_blue = 14

valid_id_sum = 0
for i in example:
    print(i)
    game, records = i.split(':')
    game_id = game.split(' ')[1]
    invalid = False

    for record in records.split(';'):
        for cube in record.split(','):
            split = cube.split(' ')
            num_of_cubes = int(split[1])
            color = split[2]
            if color == 'blue':
                if num_of_cubes > max_blue:
                    invalid = True
                    break
            elif color == 'red':
                if num_of_cubes > max_red:
                    invalid = True
                    break
            elif color == 'green':
                if num_of_cubes > max_green:
                    invalid = True
                    break
        if invalid:
            break
    if invalid == False:
        valid_id_sum += int(game_id)
        print(valid_id_sum)
print(valid_id_sum)
