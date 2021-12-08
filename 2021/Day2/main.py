class submarine:
    def __init__(self, pos=0, depth=0, aim=0):
        self.pos = pos
        self.depth = depth
        self.aim = aim

    def location(self):
        return f"At {self.pos} with depth {self.depth} and aim {self.aim}"

    def mult(self):
        return self.depth * self.pos

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x

    def forward(self, x):
        self.pos += x
        self.depth += (x * self.aim)

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