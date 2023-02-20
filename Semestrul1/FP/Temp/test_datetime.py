def divide(list):
    """

    :param list: List of elements
    :type list: string
    :return: 1 sau 0
    """
    if len(list) == 1:
        if list[0] % 2 == 1:
            return 1
        else:
            return 0
    else:
        m = len(list) // 2
        st = divide(list[m:])
        dr = divide(list[:m])
        return max(divide(st), divide(dr))


arr = [2, 4, 6, 8, 10, 20]

print(divide(arr))


