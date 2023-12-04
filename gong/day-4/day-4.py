# type: ignore

def parser() -> [[str]]:
    with open("input","r") as fhand:
        t:[[str]] = [line.strip().split("|") for line in fhand]
    return [(el[0].split(":")[0].lstrip("Card "), el[0].split(":")[1].strip().split(" "), el[1].strip().split(" ")) for el in t]

def sanitise(parsed:[[str]]) -> [[int]]:
    return [([int(b) for b in el[0]], [int(i) for i in el[1] if i != ""], [int(q) for q in el[2] if q != ""]) for el in parsed]

def a() -> None:
    tot:[float] = []
    parsed:[[int]] = sanitise(parser())
    for game in parsed:
        tem:float = 0.5
        for num in game[2]:
            if num in game[1]:
                tem = tem * 2
        if tem != 0.5:
            tot.append(int(tem))
    return sum(tot)

print(a())

# do part b later 
