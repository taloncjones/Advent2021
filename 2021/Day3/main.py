class Data:
    def __init__(self, input):
        self.filelength = 1
        self.values = [input]
        self.sums = [int(c) for c in input]
        self.gamma, self.epsilon, self.o2, self.co2 = 0, 0, 0, 0

    def parse(self, input):
        self.filelength += 1
        self.values.append(input)
        for i, c in enumerate(input):
            self.sums[i] += int(c)

    def find_GE(self):
        gamma_srt, epsilon_str = "", ""
        for i in self.sums:
            gamma_srt += "1" if (i > (self.filelength / 2)) else "0"

        for i in gamma_srt:
            epsilon_str += "0" if int(i) else "1"

        self.gamma, self.epsilon = int(gamma_srt, 2), int(epsilon_str, 2)

    def find_O2CO2(self):
        o2, co2 = self.values.copy(), self.values.copy()
        o2_str, co2_str = "", ""

        for i in range(len(self.values[0])):
            o2_count, co2_count = sum(int(x[i]) for x in o2), sum(int(x[i]) for x in co2)

            o2_str += "1" if (o2_count >= (len(o2) / 2)) else "0"
            co2_str += "0" if (co2_count >= (len(co2) / 2)) else "1"

            if len(o2) > 1:
                o2[:] = [x for x in o2 if x.startswith(o2_str)]
            if len(co2) > 1:
                co2[:] = [x for x in co2 if x.startswith(co2_str)]

        self.o2, self.co2 = int(o2[0], 2), int(co2[0], 2)            


    def power_consumption(self):
        return self.gamma * self.epsilon

    def life_support(self):
        return self.o2 * self.co2


def main():
    data = None
    with open("input.txt", "r") as file:
        for line in file:
            if not data:
                data = Data(line.rstrip())
            else:
                data.parse(line.rstrip())

    data.find_GE()

    print(f"Power: {data.power_consumption()}")

    data.find_O2CO2()

    print(f"Life: {data.life_support()}")


if __name__ == "__main__":
    main()
