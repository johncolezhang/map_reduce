import sys

if __name__ == "__main__":
    a = sys.stdin.readline().strip()
    a = str(a).split()
    count = 2
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0
    max5 = 0

    for i in range(int(a[0])):
        line = sys.stdin.readline().strip()
        line = str(line).split()
        if max1 < int(line[0]):
            max1 = int(line[0])
        if max2 < int(line[1]):
            max2 = int(line[1])
        if max3 < int(line[2]):
            max3 = int(line[2])
        if max4 < int(line[3]):
            max4 = int(line[3])
        if max5 < int(line[4]):
            max5 = int(line[4])
    print(max1 + max2 + max3 + max4 + max5)
