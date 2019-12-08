from itertools import permutations


class IntcodeEmulator:
    POSITION_MODE = '0'
    IMMEDIATE_MODE = '1'

    def __init__(self, instructions, phase_setting) -> None:
        self.instructions = instructions
        self.phase_setting = phase_setting
        self.last_output = None
        self.input_signal = None
        self.halted = False
        self.pointer = 0
        self.has_phase_setting = False

    def get_value(self, mode, ptr_offset) -> int:
        try:
            value = int(self.instructions[self.pointer + ptr_offset])
            if mode == self.POSITION_MODE:
                return int(self.instructions[value])
            else:
                return value
        except IndexError:
            return None

    def set_input_signal(self, signal) -> None:
        self.input_signal = signal

    def run(self) -> int:
        while self.instructions[self.pointer] != '99':
            instruction = self.instructions[self.pointer].rjust(5, '0')
            op = instruction[-2:]
            modes = instruction[:-2]

            arg0 = self.get_value(modes[-1], 1)
            arg1 = self.get_value(modes[-2], 2)
            dest = self.get_value(self.IMMEDIATE_MODE, 3)

            if op == '01':
                # add
                self.instructions[dest] = str(arg0 + arg1)
                self.pointer += 4

            elif op == '02':
                # mul
                self.instructions[dest] = str(arg0 * arg1)
                self.pointer += 4

            elif op == '03':
                # mov
                dest = self.get_value(self.IMMEDIATE_MODE, 1)
                if self.has_phase_setting:
                    self.instructions[dest] = str(self.input_signal)
                else:
                    self.instructions[dest] = str(self.phase_setting)
                    self.has_phase_setting = True

                self.pointer += 2

            elif op == '04':
                # mov?
                dest = self.get_value(self.IMMEDIATE_MODE, 1)
                self.last_output = int(self.instructions[dest])

                self.pointer += 2

                return self.last_output

            elif op == '05':
                # jnz
                if arg0:
                    self.pointer = arg1
                else:
                    self.pointer += 3

            elif op == '06':
                # jz
                if not arg0:
                    self.pointer = arg1
                else:
                    self.pointer += 3

            elif op == '07':
                # lt
                if arg0 < arg1:
                    self.instructions[dest] = '1'
                else:
                    self.instructions[dest] = '0'
                self.pointer += 4

            elif op == '08':
                # eq
                if arg0 == arg1:
                    self.instructions[dest] = '1'
                else:
                    self.instructions[dest] = '0'
                self.pointer += 4

        self.halted = True
        return self.last_output


with open('input.txt') as f:
    intcodes = f.read().strip().split(',')
mx = 0

for perm in permutations('56789'):
    emulators = [IntcodeEmulator(intcodes.copy(), perm[i]) for i in range(5)]
    emulators[0].set_input_signal(0)
    emulators[0].run()
    last_output = emulators[0].last_output

    for i in range(1, 5):
        emulators[i].set_input_signal(last_output)
        emulators[i].run()
        last_output = emulators[i].last_output

    i = 0
    while not emulators[-1].halted:
        emulators[i].set_input_signal(last_output)
        emulators[i].run()
        last_output = emulators[i].last_output
        i = (i + 1) % 5

    mx = max(emulators[-1].last_output, mx)
print(mx)
