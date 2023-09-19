def function_1(i):
    w = 0
    for q in i:
        w += q
    return w


def dis(a, b, c):
    D = b ** 2 - 4 * a * c
    return D


def koren(D, a, b):
    if (D > 0):
        x_1 = (-b + D ** (1/2)) / 2 / a
        x_2 = (-b - D ** (1/2)) / 2 / a
        return x_1, x_2
    elif (D == 0):
        return -b/2/a
    else:
        raise Exception


if __name__ == '__main__':
    b = []
    n = 0
    # while True:
    #     b.append(int(input()))
    #     if b[n] == 0:
    #         break
    #     n += 1
    print("a")
    a = int(input())
    print("b")
    b = int(input())
    print("c")
    c = int(input())
    try:
        koren(dis(a, b, c), a, b)
    except Exception:
        print('No solutions')
