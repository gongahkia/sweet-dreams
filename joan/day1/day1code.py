# input processing
def convert(mapfile):
    
    with open(mapfile,'r') as f:
        lines = []
        
        for line in f:
            extract = line.rstrip('\n')
            lines.append(extract)
            
    return lines

def foo(file):
    fnums = []
    strnum = ["0","1","2","3","4","5","6","7","8","9"]

    for line in file:
        digits = []
        for char in line:
            # extraction of numbers from a line
            if char in strnum:
                digits.append(char)
            else:
                continue
        # get 2 digit number from each line
        tgt = str(digits[0] + digits[-1])
        final = int(tgt)
        fnums.append(final)
        
    # obtain sum
    fsum = 0
    for nums in fnums:
        fsum += nums
        
    return fsum

inp = convert("day1.txt")
print(foo(inp))
