import AOC


def makeVectorPath(wire: list) -> list:
    dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

    point = (0, 0)
    path = {point}

    for p in wire:
        direction = p[0]
        magnitude = int(p[1:])
        for i in range(magnitude):
            point = (point[0] + dx[direction], point[1] + dy[direction])
            path.add(point)

    return path


path1 = makeVectorPath(AOC.wire1)
path2 = makeVectorPath(AOC.wire2)

min_distance = 2 ** 32
intersection = None

for t in path1:
    if t in path2:
        dist = abs(t[0]) + abs(t[1])
        if dist < min_distance and dist != 0:
            intersection = t
            min_distance = dist

print(min_distance)
print(intersection)
