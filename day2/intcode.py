class IntCode:
    """
    IntCode class
    """
    def __init__(self, data):
        """
        Constructor
        Args:
            data: a list of memory values
        """
        print(data)
        self.data = [int(x) for x in data]
        self.memory_pointer = 0
        while self.data[self.memory_pointer] != 99:
            self.do_op()
        print(self.data)
        print("the result is : ",self.data[0])

    def do_op(self):
        """
        does the operation depending on the value at the current memory pointer
        and the 3 after it
            op 1: add the number at memory pointer + 1 to the number at memory pointer + 2
            and place this at the place pointing to memory pointer + 3
            op 2: the same but then multiplying instead of adding
        """
        curr_pointer = self.memory_pointer
        code = self.data[curr_pointer]
        data1 = self.data[self.data[curr_pointer + 1]]
        data2 = self.data[self.data[curr_pointer + 2]]
        result = None
        if code == 1:
            # Addition
            result = data1 + data2
        elif code == 2:
            # Multiplication
            result = data1 * data2
        else:
            print("ERROR!!")
        print(f"code: {code}, data1: {data1}, data2: {data2}, result: {result}\n{self.data}")
        self.data[self.data[curr_pointer + 3]] = result
        self.memory_pointer += 4