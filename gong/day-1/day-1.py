# type: ignore

valid:{str} = {"one":"1",
               "two":"2", 
               "three":"3", 
               "four":"4", 
               "five":"5", 
               "six":"6", 
               "seven":"7", 
               "eight":"8", 
               "nine":"9"}

def a() -> int:
    with open("input", "r") as fhand:
        fin:[[int]]= [[int(char) for char in line if char.isnumeric()] for line in (line.rstrip() for line in fhand)]
    return sum(int(str(val[0]) + str(val[-1])) if len(val) > 1 else int(str(val[0]) * 2) for val in fin)

# DEBUG THIS SHIT
def b() -> int:
    fhand = open("input","r")
    fin:[[str]] = []
    for line in [line.rstrip() for line in fhand]:
        tem:[str] = []
        buffer:str = ""
        for q in range(len(line)):
            if line[q].isnumeric():
                # print(f"{char} NUMERIC")
                tem.append(line[q])
            else:
                # print(f"{char} BUFFER and {buffer}")
                buffer += line[q]
                if "one" in buffer:
                    tem.append("1")
                    buffer = ""
                elif "two" in buffer:
                    tem.append("2")
                    buffer = ""
                elif "three" in buffer:
                    tem.append("3")
                    buffer = ""
                elif "four" in buffer:
                    tem.append("4")
                    buffer = ""
                elif "five" in buffer:
                    tem.append("5")
                    buffer = ""
                elif "six" in buffer:
                    tem.append("6")
                    buffer = ""
                elif "seven" in buffer:
                    tem.append("7")
                    buffer = ""
                elif "eight" in buffer:
                    tem.append("8")
                    buffer = ""
                elif "nine" in buffer:
                    tem.append("9")
                    buffer = ""
                else:
                    pass
        fin.append(tem)
    fhand.close()
    sum = 0
    for val in fin:
        if len(val) == 1:
            sum += int(val[0] + val[0])
        else:
            sum += int(val[0] + val[-1])
    print(fin)
    return sum


print(a())
print(b())


