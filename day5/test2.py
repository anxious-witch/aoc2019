def get_val(mode, val, codes) -> int:
    val = int(val)

    if mode == '0':
        return int(codes[val])
    else:
        return val


def main(n, test=False):
    if test:
        with open('test.txt') as f:
            intcodes = f.read().strip().split(',')
    else:
        with open('input.txt') as f:
            intcodes = f.read().strip().split(',')

    p = 0
    while intcodes[p] != '99':
        opmode = intcodes[p].rjust(5, '0')
        op = opmode[-2:]
        mode = opmode[:-2]

        if op == '01':
            # add
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)
            dest = int(intcodes[p + 3])
            intcodes[dest] = str(arg0 + arg1)
            p += 4

        elif op == '02':
            # mul
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)
            dest = int(intcodes[p + 3])
            intcodes[dest] = str(arg0 * arg1)
            p += 4

        elif op == '03':
            # mov
            dest = int(intcodes[p + 1])
            intcodes[dest] = str(n)
            p += 2

        elif op == '04':
            # mov?
            dest = int(intcodes[p + 1])
            print('DIAG: ', intcodes[dest])
            p += 2

        elif op == '05':
            # jnz
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)

            if arg0:
                p = arg1
            else:
                p += 3

        elif op == '06':
            # jz
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)

            if not arg0:
                p = arg1
            else:
                p += 3

        elif op == '07':
            # lt
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)

            dest = int(intcodes[p + 3])

            if arg0 < arg1:
                intcodes[dest] = '1'
            else:
                intcodes[dest] = '0'
            p += 4

        elif op == '08':
            # eq
            arg0 = get_val(mode[-1], intcodes[p + 1], intcodes)
            arg1 = get_val(mode[-2], intcodes[p + 2], intcodes)

            dest = int(intcodes[p + 3])

            if arg0 == arg1:
                intcodes[dest] = '1'
            else:
                intcodes[dest] = '0'
            p += 4


main(5)
