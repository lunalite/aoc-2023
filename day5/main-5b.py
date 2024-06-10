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

seeds_range = [int(x) for x in example[0].split(':')[1].strip().split(' ')]
seeds = []
for i in range(0, len(seeds_range), 2):
    seeds.append((seeds_range[i], seeds_range[i + 1]))

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
q = 0
for m in maps[:-1]:
    max_seed_length = len(seeds)
    new_seeds = []
    while len(seeds) > 0:
        seed, seed_range = seeds.pop()
        marked = False
        for defined_range in m:
            min_seed_range = int(seed)
            max_seed_range = int(seed) + int(seed_range)
            min_defined_range = int(defined_range[1])
            max_defined_range = min_defined_range + int(defined_range[2])
            mapped_min = int(defined_range[0])
            print(seed, seed_range)
            print(defined_range)
            if min_defined_range <= min_seed_range and max_seed_range <= max_defined_range:
                print('y1')
                new_seeds.append(((min_seed_range - min_defined_range + mapped_min), seed_range))
                marked = True
                break
            elif min_seed_range <= min_defined_range and max_defined_range <= max_seed_range:
                print('y2')
                seeds.append((min_seed_range, min_defined_range - min_seed_range))
                new_seeds.append((mapped_min, int(defined_range[2])))
                seeds.append((max_defined_range, max_seed_range - max_defined_range))
                marked = True
                break
            elif min_defined_range <= min_seed_range < max_defined_range:
                print('y3')
                new_seeds.append((min_seed_range - min_defined_range + mapped_min, max_defined_range - min_seed_range))
                seeds.append((max_defined_range, max_seed_range - max_defined_range))
                marked = True
                break
            elif min_defined_range < max_seed_range <= max_defined_range:
                print('y4')
                seeds.append((min_seed_range, (min_defined_range - min_seed_range)))
                new_seeds.append((mapped_min, max_seed_range - min_defined_range))
                marked = True
                break
        if not marked:
            new_seeds.append((seed, seed_range))
        print(new_seeds)
        print('\n')
    seeds = new_seeds
    print(seeds)


print(min(seeds))
