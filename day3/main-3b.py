document = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

example = []
for i in document.split('\n'):
    c = []
    for j in i:
        c.append(j)
    example.append(c)


def check(r, c, d):
    if r < 0 or r >= len(example) or c < 0 or c >= len(example[0]):
        return d
    if example[r][c].isdigit():
        to_add = example[r][c]
        example[r][c] = '.'
        d = check(r, c - 1, d) + to_add + check(r, c + 1, d)
    return d


sum_of_digit = 0
for row_num in range(len(example)):
    row = example[row_num]
    for col_num in range(len(row)):
        col = row[col_num]
        if col == '*':
            digits = []
            for r_change, c_change in [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]:
                check1 = check(row_num + r_change, col_num + c_change, '')
                if check1 != '':
                    print(check1)
                    digits.append(int(check1))
            if len(digits) == 2:
                sum_of_digit += digits[0] * digits[1]

print(sum_of_digit)
