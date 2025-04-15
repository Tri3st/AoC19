class OpCodeCompiler:
    def __init__(self, data, inp):
        self.data = [int(x) for x in data]
        self.input = inp
        self.output = None
        self.mem = 0
        self.stop = False
        print("data : ", self.data)
        while self.data[self.mem] != 99 or self.stop:
            self.do_op()
        print("Output : ", self.output)

    def do_op(self):
        opstr = [int(x) for x in list(str(self.data[self.mem]))]
        print("Opstr : ", opstr)
        op, val1, val2, val3, mod1, mod2, mod3 = None, None, None, None, None, None, None
        if len(opstr) == 1:
            op = int(opstr, 10)
            if op == 3:
                self.data[self.mem + 1] = self.input
                self.mem += 2
            else:
                # op == 4
                self.output = self.data[self.mem + 1]
                self.mem += 2
                self.stop = True
        else:
            if len(opstr) == 4:
                opstr.insert(0, 0)
                op = int("".join(str(x) for x in opstr[3:]))
            else:
                # len(opstr) == 5:
                op = int(opstr[-2:])
            mod1 = int(opstr[2])
            mod2 = int(opstr[1])
            mod3 = int(opstr[0])
            val1 = self.data[self.mem + 1] if mod1 == 0 else self.mem + 1
            val2 = self.data[self.mem + 2] if mod2 == 0 else self.mem + 2
            if op == 1:
                # add
                val3 = val1 + val2
                if mod3 == 0:
                    self.data[self.data[self.mem + 3]] = val3
                else:
                    self.data[self.mem + 3] = val3
                self.mem += 4
            elif op == 2:
                # multiply
                val3 = val1 * val2
                if mod3 == 0:
                    self.data[self.data[self.mem + 3]] = val3
                else:
                    self.data[self.mem + 3] = val3
                self.mem += 4
