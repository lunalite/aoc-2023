import re

document = """Time:      7  15   30
Distance:  9  40  200"""

example = document.split('\n')

times = []
distances = []

for j in re.findall('\d+', example[0]):
    times.append(int(j))
for j in re.findall('\d+', example[1]):
    distances.append(int(j))

all_the_ways = []
for case in range(len(times)):
    distance_to_beat = distances[case]
    max_time = times[case]

    ways = 0
    for t_hold in range(1, max_time + 1):
        if (max_time - t_hold) * t_hold > distance_to_beat:
            ways += 1
    all_the_ways.append(ways)

multi = 1
for w in all_the_ways:
    multi *= w
print(multi)
