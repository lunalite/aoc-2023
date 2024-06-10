import re

document = """Time:        51     69     98     78
Distance:   377   1171   1224   1505"""

example = document.split('\n')

t = ''
d = ''
for j in re.findall('\d+', example[0]):
    t += j
for j in re.findall('\d+', example[1]):
    d += j
time = int(t)
distance = int(d)

print(time, distance)

low = 0
high = time

while True:
    current = low + int((high - low) / 2)
    if high - low <= 1:
        current = high
        break
    if (time - current) * current > distance:
        high = current
    else:
        low = current

mmin = current

low = 0
high = time

while True:
    current = low + int((high - low) / 2)
    if high - low <= 1:
        current = low
        break
    if (time - current) * current > distance:
        low = current
    else:
        high = current

mmax = current
print(mmin, mmax)
print(mmax - mmin + 1)
