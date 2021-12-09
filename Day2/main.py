class submarine:
    def __init__(self, pos=0, depth=0):
        self.pos = pos
        self.depth = depth

    def location(self):
        return f"At {self.pos} with depth {self.depth}"

    def mult(self):
        return self.depth * self.pos

    def down(self, x):
        self.depth += x

    def up(self, x):
        self.depth -= x

    def forward(self, x):
        self.pos += x

    def back(self, x):
        self.pos -= x

def main():
    sub = submarine()

    f = open("input.txt", "r")

    for line in f:
        parse = line.split()
        cmd, x = parse[0], int(parse[1])
        func = getattr(sub, cmd)
        func(x)

    print(sub.mult())


if __name__ == "__main__":
    main()