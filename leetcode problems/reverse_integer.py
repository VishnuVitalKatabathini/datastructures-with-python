def reverse(x):
    val = str(x)
    length = len(val)
    if '-' == val[0]:
        rev = val[-1:-length:-1]
        res = -int(rev)
        range = -2 ** 31
        if res < range:
            return 0
        return res
    else:
        rev = val[-1:-(length + 1):-1]
        res = int(rev)
        range = 2 ** 31 - 1
        if res > range:
            return 0
        else:
            return res


print(reverse(int(input('enter a number'))))
