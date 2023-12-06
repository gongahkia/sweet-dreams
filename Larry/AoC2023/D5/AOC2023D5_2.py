"""
def problem_5_2():
    --- Part Two ---
    Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

    The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

    seeds: 79 14 55 13
    This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

    Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

    In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D5\\AOC23D5_test_2.txt"


def process_data(Rawdata):
    maps = tuple([i.split(":")[1] for i in Rawdata])
    changes = [i.split(":")[0] for i in Rawdata][1:]
    changes = [i.replace(" map", "") for i in changes]
    origin_list = maps[0].split(" ")
    seeds = [int(i) for i in origin_list if i != '']
    print()
    print("-"*30)
    maps2 = maps[1:]

    maps2 = [conversion.split("\n") for conversion in maps2]
    maps = []

    for conversion in maps2:
        thing = []
        for row in conversion:
            if row == "":
                continue
            else:
                row = row.split(" ")
                row = [int(b) for b in row if b != ""]
                dr, sr, steps = row

                thing.append([dr, (sr, sr+steps-1)])
        maps.append(thing)

    # * seeds into seed ranges
    newseeds = []
    seed1 = seeds[::2]
    seed2 = seeds[1::2]
    for i in range(len(seed1)):
        newseeds += [(seed1[i], seed1[i]+seed2[i]-1)]

    print(f"""maps: {maps}\n\n\nchanges : {changes}\n\n\nnewseeds: {newseeds}\n\n""")
    return maps, changes, newseeds


def plant_plant_plant_plant_get_planted_get_planted_2(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    # step 1: processing data
    Rawdata = r.split("\n\n")
    maps, changes, seeds = process_data(Rawdata)
    print(maps, changes, seeds, sep='\n\n')

    row, conversion = [], []
    # ? to watch list
    # for i in maps:
    # print(i)

    for cnum in range(len(maps)):
        conversion = maps[cnum]
        change = changes[cnum]
        origin = seeds[:]
        modded = seeds[:]
        final = seeds[:]
        for row in conversion:
            print(f"current seedstate:\t{seeds}\t{change.split("-")[0]}")
            print()
            print(f"conversion row:\t\t{row}\t{change}")
            print()

            destination, source = row
            o_start, o_end = source
            for i in range(len(origin)):
                seedrange = seeds[i]
                seedstart,seedend = seedrange
                
                # * Seedrange    (79, 92)
                # * origin range (98, 99)
                
                #!Case 2: seed range within origin range
                if o_start <= seedstart and o_end >= seedend:
                    
                
                
                if origval >= o_start and origval <= o_end:
                    modded[i] += (destination-o_start)

    #        for i in range(len(seeds)):
    #            if origin_list[i] != modded[i]:
    #                thing = modded.copy()
    #                final_list[i] = thing[i]
    #        modded = seeds[:]
    #        print(f"new seedstate:\t\t{seeds[3]}\t{change.split("-")[2]}")
    #        print()
    #        print("-"*30)
    #        print()
    #    seeds = final_list[:]

    # * return lowest location number that corresponds to any of the initial seed numbers?
    # return min(seeds)
print(plant_plant_plant_plant_get_planted_get_planted_2(test2))
