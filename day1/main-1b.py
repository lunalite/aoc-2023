document = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

example = document.split('\n')


def word_is_num(sub_list):
    if len(sub_list) < 3:
        return 0
    try:
        if sub_list[0:3] == 'one':
            return 1
        elif sub_list[0:3] == 'two':
            return 2
        elif sub_list[0:5] == 'three':
            return 3
        elif sub_list[0:4] == 'four':
            return 4
        elif sub_list[0:4] == 'five':
            return 5
        elif sub_list[0:3] == 'six':
            return 6
        elif sub_list[0:5] == 'seven':
            return 7
        elif sub_list[0:5] == 'eight':
            return 8
        elif sub_list[0:4] == 'nine':
            return 9
    except:
        return 0
    return 0


sum = 0
for i in example:
    first = 's'
    second = 's'
    for j in range(len(i)):
        if i[j].isdigit():
            first = i[j]
            break
        elif word_is_num(i[j:]) != 0:
            first = word_is_num(i[j:])
            break

    for j in range(len(i) - 1, -1, -1):
        if i[j].isdigit():
            second = i[j]
            break
        elif word_is_num(i[j:]) != 0:
            second = word_is_num(i[j:])
            break
    sum += int(f'{first}{second}')
print(sum)
