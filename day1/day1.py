
with open("day1p2Input.txt") as f:
    lines = f.readlines()
# fun note: .*?(\d|one|two|three|four|five|sixe|seven|eight|nine).*(\d|one|two|three|four|five|sixe|seven|eight|nine).*?
# this is the regex to do this
lookup = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "0":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

lineNums = []
for line in lines:
    first = {}
    last = {}

    for k in lookup.keys():
        first[line.find(k)] = k
        last[line.rfind(k)] = k
    
    if -1 in first:
        del first[-1]
    
    lineNums.append(int(lookup[first[min(first.keys())]] + lookup[last[max(last.keys())]]))

print(sum(lineNums))