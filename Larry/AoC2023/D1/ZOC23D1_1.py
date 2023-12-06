"""
def problem_1_1():
    --- Day 1: Trebuchet?! ---
    Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

    You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

    As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

    The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D1\\AOC23D1_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D1\\AOC23D1_test_1.txt"

def sky_coords(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()
    R = r.split("\n")

    final = []

    for i in R:
        stor = []
        for q in i:
            if q.isdigit():
                stor.append(q)
                break

        I = i[::-1]
        for q in I:
            if q.isdigit():
                stor.append(q)
                break

        thing = int(''.join(stor))

        final.append(thing)
        stor.clear()

    return sum(final)


print(sky_coords(filename))
