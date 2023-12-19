with open("day2p1Input.txt") as f:
    lines = f.readlines()

games = []

for line in lines:
    idx = line.index(":")
    pulls = line[idx + 1:].strip().split(";")
    game = {}
    for pull in pulls:
        colors = pull.strip().split(",")
        for color in colors:
            [num, code] = color.strip().split(" ")
            if code not in game:
                game[code] = []
            game[code].append(int(num))
    games.append(game)
    print(game)

possible = []
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
for i,game in enumerate(games):
    if max(game["red"]) <= MAX_RED and max(game["green"]) <= MAX_GREEN and max(game["blue"]) <= MAX_BLUE:
        possible.append(i + 1)
print(possible)
print(sum(possible))
