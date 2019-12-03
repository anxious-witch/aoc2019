from AOC import l


def run(intcodes: list, a: int, b: int) -> int:
    lim = len(intcodes) // 4 + 1

    intcodes[1] = a
    intcodes[2] = b

    for i in range(lim):
        index = i * 4
        opcode = intcodes[index]

        if opcode == 99:
            return intcodes[0]

        try:
            intcodes[intcodes[index + 3]] = manipulate(
                opcode,
                intcodes[intcodes[index + 1]],
                intcodes[intcodes[index + 2]]
            )
        except:
            return 0


def manipulate(opcode: int, a: int, b: int) -> int:
    if opcode == 1:
        return a + b
    elif opcode == 2:
        return a * b


for x in range(100):
    for y in range(100):
        copied = l.copy()
        if run(copied, x, y) == 19690720:
            print(100 * x + y)
