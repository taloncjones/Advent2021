def main():
    prev, count = float("inf"), 0
    f = open("input.txt", "r")

    for value in f:
        if prev < int(value):
            count += 1
        prev = int(value)

    print(count)

if __name__ == "__main__":
    main()