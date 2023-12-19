with open("day2p2Input.txt") as f:
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
for i,game in enumerate(games):
    possible.append(max(game["red"]) * max(game["blue"]) * max(game["green"]))
print(possible)
print(sum(possible))
