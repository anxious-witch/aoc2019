import AOC


def makeVectorPath(wire: list) -> list:
    dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

    point = (0, 0)
    path = {point}
    steps = 0

    stepMap = dict()

    for p in wire:
        direction = p[0]
        magnitude = int(p[1:])
        for i in range(magnitude):
            steps += 1
            point = (point[0] + dx[direction], point[1] + dy[direction])
            path.add(point)

            if point in stepMap:
                if stepMap[point] > steps:
                    stepMap[point] = steps
            else:
                stepMap[point] = steps

    return path, stepMap


path1, stepMap1 = makeVectorPath(AOC.wire1)
path2, stepMap2 = makeVectorPath(AOC.wire2)

min_steps = 2 ** 32
intersection = None

for t in path1:
    if t in path2 and t != (0, 0):
        steps = stepMap1[t] + stepMap2[t]
        if steps < min_steps:
            intersection = t
            min_steps = steps

print(min_steps)
print(intersection)
