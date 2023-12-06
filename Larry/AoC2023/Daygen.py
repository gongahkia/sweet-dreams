import os
import datetime


#! Code assumes that its in the folder where you wanna work in.

# **Get Year and Date, leave blank if creating for current day
Year = input("Enter Year (if current year, then leave blank)")
Day = input("Enter Day to create input for, else leave blank")

Today = datetime.date.today()
Year = int(str(Today).split("-")[0]) if Year == "" else Year
print(Year)
Day = int(str(Today).split("-")[2]) if Day == "" else Day
#print(Day)

Day = 7;print(Day)

scriptnames = ["AOC", "_input.txt", "_test_1.txt", "_test2.txt",]

dirname = os.path.dirname(__file__)

foldername = dirname + f"\\D{Day}"

print(f"The directory's name is {dirname}")

if os.path.exists(foldername):
    print("Directory already exists, please make sure day has been completed.")
    exit()

os.makedirs(foldername)

#* ok im lazy to do this properly paiseh

#* 1 - create input dump file
filename = foldername + f"\\AOC{Year[1:]}D{Day}{scriptnames[1]}"
with open(filename) as f:
    f.write("Replace_with_input")

#* 2 - create testcase1 dump file
filename = foldername + f"\\AOC{Year[1:]}D{Day}{scriptnames[2]}"
with open(filename) as f:
    f.write("Replace_with_testinput1")

#* 3 - create testcase2 dump file
filename = foldername + f"\\AOC{Year[1:]}D{Day}{scriptnames[2]}"
with open(filename) as f:
    f.write("Replace_with_testinput2")



f"""
def problem_{Day}_1():
    Paste_qn_statement
"""

filename = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_input.txt"

test = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_1.txt"
test2 = "C:\\Users\\ChunChunMaru\\Desktop\\Baby code\\FeetV2\\AoC\\AoC2023\\D6\\AOC23D6_test_2.txt"

rubbish = f"""\"\"\"
def problem_6_1():
    dump_qn_statement_here
\"\"\"

def process_data(RD):
    # * dump data for processing here
    return relevant_data

def problem6_1(filename):
    with open(filename) as f:
        r = f.read()
    r.strip()

    Rawdata = r.split("\n")
    # step 1: processing data
    
    #! swap out with actual data
    var_name = process_data(Rawdata)
    
    return thing

print(wishin_i_was_fishin(test))

"""





#* 4 - create problem 1 script file
filename = foldername + f"\\AOC{Year}D{Day}_1.py"
with open(filename) as f:
    f.write(lazyconvert)
