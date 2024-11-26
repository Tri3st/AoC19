class NanoNode:
    def __init__(self, name):
            self.name = name
            self.l = None
            self.r = None


class NanoFactory:
    def __init__(self):
        self.nanotree = NanoNode("Fuel")

