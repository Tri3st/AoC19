class OpCodeCompiler:
    def __init__(self, data, inp):
        self.data = [int(x) for x in data]
        self.input = inp
        self.output = []
        self.mem = 0
        self.stop = False
        print("data : ", self.data)
        while self.data[self.mem] != 99:
            self.do_op()
        print("Output : ", self.output)

    def do_op(self):
        """
            mode: 0 -> position mode 50 means store it in memory pos 50
                  1 -> immediate mode 50 means store 50 in this place
        """
        op_lst = [int(x) for x in list(str(self.data[self.mem]))]
        op, mod1, mod2, mod3, val1, val2, val3 = None, None, None, None, None, None, None
        if len(op_lst) == 4:
            op_lst.insert(0, 0)
        elif len(op_lst) == 3:
            op_lst.insert(0, 0)
            op_lst.insert(2, 0)
        elif len(op_lst) == 2:
            op_lst.insert(0, 0)
            op_lst.insert(1, 0)
            op_lst.insert(3, 0)
        if len(op_lst) > 1:
            print("op_lst : ", op_lst)
            op = int("".join([str(n) for n in op_lst[3:]]), 10)
            mod1 = op_lst[2]
            mod2 = op_lst[1]
            mod3 = op_lst[0]
            val1 = self.data[self.data[self.mem + 1]] if mod1 == 0 else self.data[self.mem + 1]
            val2 = self.data[self.data[self.mem + 2]] if mod2 == 0 else self.data[self.mem + 2]
        else:
            op = op_lst[0]
            if op < 3:
                mod1 = 0
                mod2 = 0
                mod3 = 0
                val1 = self.data[self.data[self.mem + 1]]
                val2 = self.data[self.data[self.mem + 2]]

        if op == 1:
            # Add
            val3 = val1 + val2
            if mod3 == 0:
                self.data[self.data[self.mem + 3]] = val3
            else:
                self.data[self.mem + 3] = val3
            self.mem += 4
        elif op == 2:
            # Multiply
            val3 = val1 * val2
            if mod3 ==0:
                self.data[self.data[self.mem + 3]] = val3
            else:
                self.data[self.mem + 3] = val3
            self.mem += 4
        elif op == 3:
            # Input
            self.data[self.data[self.mem + 1]] = self.input
            self.mem += 2
            print(f"op: {op}, input: {self.input}, mem: {self.mem}")
        elif op == 4:
            # Output
            self.output.append(self.data[self.data[self.mem + 1]])
            self.mem += 2
            print(f"op: {op}, output: {self.output[-1]}, mem: {self.mem}")
            self.stop = True
        else:
            # Invalid opcode
            raise ValueError('Invalid opcode')
        if op < 3:
            print(f"op: {op}, val1: {val1}({mod1}), val2: {val2}({mod2}), val3: {val3}({mod3}), mem: {self.mem}")
        print(self.data)

