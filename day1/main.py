document = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

example = document.split('\n')

sum = 0
for i in example:
    first = 's'
    second = 's'
    for j in range(len(i)):
        if i[j].isdigit():
            first = i[j]
            break

    for j in range(len(i)-1, -1, -1):
        if i[j].isdigit():
            second = i[j]
            break

    sum += int(f'{first}{second}')
print(sum)
