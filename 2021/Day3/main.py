class Data:
    def __init__(self, input):
        self.filelength = 1
        self.sums = [int(c) for c in input]
        self.gamma, self.epsilon = 0, 0

    def parse(self, input):
        self.filelength += 1
        for i, c in enumerate(input):
            self.sums[i] += int(c)

    def find_GE(self):
        gamma_srt, epsilon_str = "", ""
        for i in self.sums:
            gamma_srt += "1" if (i > (self.filelength / 2)) else "0"

        for i in gamma_srt:
            epsilon_str += "0" if int(i) else "1"

        self.gamma, self.epsilon = int(gamma_srt, 2), int(epsilon_str, 2)

    def power_consumption(self):
        return self.gamma * self.epsilon


def main():
    data = None
    with open("input.txt", "r") as file:
        for line in file:
            if not data:
                data = Data(line.rstrip())
            else:
                data.parse(line.rstrip())

    data.find_GE()

    print(data.power_consumption())


if __name__ == "__main__":
    main()
