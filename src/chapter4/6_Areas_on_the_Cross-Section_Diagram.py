def calcurate(string):
    stack1 = []
    stack2 = []
    area = 0
    for idx, char in enumerate(string):
        if char == "\\":
            stack1.append(idx)

        elif char == "/":
            if len(stack1) == 0:
                continue

            j = stack1.pop()
            area += idx - j
            area_ = idx - j
            while len(stack2) != 0 and stack2[-1][0] > j:
                area_ += stack2.pop()[1]
            stack2.append((j, area_))

    return area, stack2


def main():
    string = input()
    area, lakes = calcurate(string)
    print(area)
    print(len(lakes), *[lake[1] for lake in lakes])


if __name__ == "__main__":
    main()
