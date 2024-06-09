document = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

example = document.split('\n')

seeds = [int(x) for x in example[0].split(':')[1].strip().split(' ')]

maps = []


def map_string_to_maps(_idx):
    for i in example[1:]:
        if 'map' in i:
            break
        _idx += 1

    src_to_dest_list = []
    _idx += 1
    for i in example[_idx:]:
        if i == '':
            break
        src_to_dest_list.append(tuple(i.split(' ')))
        _idx += 1

    maps.append(src_to_dest_list)
    return _idx


idx = 1
while idx <= len(example):
    idx = map_string_to_maps(idx)

for m in maps[:-1]:
    for seed_idx in range(len(seeds)):
        seed = seeds[seed_idx]
        new_seed = -1
        for defined_range in m:
            if int(defined_range[1]) <= int(seed) <= int(defined_range[1]) + int(defined_range[2]):
                new_seed = int(defined_range[0]) + int(seed) - int(defined_range[1])
                seeds[seed_idx] = new_seed
                break
print(min(seeds))
