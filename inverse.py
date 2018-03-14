import sys

if __name__ == "__main__":
    line = list(sys.stdin.readline().strip())
    ord_a = ord("a")
    ord_z = ord("y")
    ord_A = ord("A")
    ord_Z = ord("Y")
    re_list = []
    for li in line:
        ord_li = ord(li)
        if ord_a <= ord_li <= ord_z:
            ord_li += 1
        if ord_A <= ord_li <= ord_Z:
            ord_li += 1
        re_list.append(ord_li)

    re_list = list(map(lambda x: chr(x), re_list))
    result = ""
    for re in re_list:
        result += re
    print(result)