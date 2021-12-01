def test(s):
    def swap(a, b, str):
        tmp = str[b]
        str[b] = str[a]
        str[a] = tmp

    length = len(s)
    array = [c for c in s]
    for i in range(int(length / 2)):
        swap(i, length-i, array)

    return ''.join(array)
