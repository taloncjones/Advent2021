def main():
    pop, count = float("inf"), 0
    window = [float("inf")]
    f = open("input.txt", "r")

    for value in f:
        window.append(int(value))
        if len(window) > 3:
            pop, window = window[0], window[1:]

        if pop < window[-1]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()