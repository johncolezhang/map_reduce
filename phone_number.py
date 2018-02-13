
digits = "23"
dict1 = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
}
strL = list(digits)
if len(strL) > 0:
    list1 = dict1[strL[0]]
    for str1 in range(1, len(strL)):
        list2 = dict1[strL[str1]]
        tmp = list1
        result = []
        for i in range(len(list2)):
            tmp = list(map(lambda x: x + list2[i], tmp))
            result.extend(tmp)
            tmp = list1
        list1 = result