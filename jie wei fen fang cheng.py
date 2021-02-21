def xoto(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a1 = (m2 - m1) * (n2 - n1)
    return a1


def x1to(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a2 = 0.5 * (m2 * m2 - m1 * m1) * (n2 - n1)
    return a2


def xot1(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a3 = 0.5 * (n2 * n2 - n1 * n1) * (m2 - m1)
    return a3


def x1t1(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a4 = 0.5 * 0.5 * (m2 * m2 - m1 * m1) * (n2 * n2 - n1 * n1)
    return a4


def x2to(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a5 = 1 / 3 * (m2 ** 3 - m1 ** 3) * (n2 - n1)
    return a5


def xot2(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    a6 = 1 / 3 * (n2 ** 3 - n1 ** 3) * (m2 - m1)
    return a6


def x2t1(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    b4 = 1 / 3 * 1 / 2 * (m2 ** 3 - m1 ** 3) * (n2 ** 2 - n1 ** 2)
    return b4


def x3to(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    b5 = 0.25 * (m2 ** 4 - m1 ** 4) * (n2 - n1)
    return b5


def x1t2(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    b6 = 0.5 * 1 / 3 * (m2 ** 2 - m1 ** 2) * (n2 ** 3 - n1 ** 3)
    return b6


def x3t1(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    c4 = 0.25 * 0.5 * (m2 ** 4 - m1 ** 4) * (n2 ** 2 - n1 ** 2)
    return c4


def x4to(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    c5 = 0.2 * (m2 ** 5 - m1 ** 5) * (n2 - n1)
    return c5


def x2t2(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    c6 = 1 / 3 * 1 / 3 * (m2 ** 3 - m1 ** 3) * (n2 ** 3 - n1 ** 3)
    return c6


def xot3(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    d6 = 0.25 * (m2 - m1) * (n2 ** 4 - n1 ** 4)
    return d6


def x1t3(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    e4 = 0.25 * 0.5 * (m2 ** 2 - m1 ** 2) * (n2 ** 4 - n1 ** 4)
    return e4


def xot4(i, j):
    m1 = i * 1 / 1000
    m2 = (i + 1) * 1 / 1000
    n1 = j * 1 / 1000
    n2 = (j + 1) * 1 / 1000
    e6 = 0.2 * (m2 - m1) * (n2 ** 5 - n1 ** 5)
    return e6


def jie(a):
    return [b]


if __name__ == '__main__':
    a = [[0 for i in range(1001)] for j in range(1001)]
    b = [[0 for i in range(1001)] for j in range(1001)]
    c = [[0 for i in range(1001)] for j in range(1001)]
    d = [[0 for i in range(1001)] for j in range(1001)]
    e = [[0 for i in range(1001)] for j in range(1001)]
    f = [[0 for i in range(1001)] for j in range(1001)]
    l1 = [[0 for i in range(6)] for j in range(6)]
    k1 = [0 for i in range(6)]
    i = 1
    j = 1
    m1 = (i - 1) * 1 / 1000
    m2 = i * 1 / 1000
    n1 = (j - 1) * 1 / 1000
    n2 = j * 1 / 1000
    z = input("请输入波速")
    while i <= 1000 and j <= 1000:
        while i <= 1000 and j <= 1000
            if j == 1
                x0 = m1
                t0 = n1
                xot0 = xoto(i - 1, j - 1)
                x1t0 = x1to(i - 1, j - 1)
                x0t1 = xot1(i - 1, j - 1)
                x0t0 = xoto(i - 1, j - 1)
                l1[0][0] = (m2 - m1) + (n2 - n1) + 0.5 * (n2 ** 2 - n1 ** 2)
                l1[0][1] = 0.5 * (m2 ** 2 - m1 ** 2) + x0 * (n2 - n1)
                l1[0][2] = 1 / 3 * (m2 ** 3 - m1 ** 3) + x0 * x0 * (n2 - n1) + 2 * (m2 - m1) * (n2 - n1)
                l1[0][3] = (m2 - m1) + t0 * (m2 - m1) + 0.5 * (n2 ** 2 - n1 ** 2)
                l1[0][4] = t0 * (m2 - m1) + 1 / 3 * (n2 ** 3 - n1 ** 3) - 2 * (n2 - n1) * (m2 - m1)
                l1[0][5] = 0.5 * (m2 ** 2 - m1 ** 2) + 0.5 * t0 * (m2 ** 2 - m1 ** 2) + 0.5 * x0 * (n2 ** 2 - n1 ** 2)
                k1[0] = -1 * a[i][j - 1] - 0.5 * b[i][j - 1] * (m2 ** -m1 ** 2) - 1 / 3 * c[i][j - 1] * (
                            m2 ** 3 - m1 ** 3) - 0.5 * t0 * f[i][j - 1] * (m2 ** 2 - m1 ** 2) - t0 * d[i][j - 1] * (
                                    m2 - m1) - t0 * (m2 - m1) * e[i][j - 1] \
                        - a[i - 1][j] * (n2 - n1) - 0.5 * d[i - 1][j] * (n2 ** 2 - n1 ** 2) - 1 / 3 * e[i - 1][j] * (
                                    n2 ** 3 - n1 ** 3) - 0.5 * f[i - 1][j] * x0 * (n2 ** 2 - n1 ** 2) - b[i - 1][
                            j] * x0 * (n2 - n1) - c[i - 1][j] * x0 * x0 * (n2 - n1)
                l1[2][1] = 0.5 * (m2 ** 2 - m1 ** 2) + x0 * (n2 - n1)
                l1[2][2] = 1 / 3 * (m2 ** 3 - m1 ** 3) + x0 * x0 * (n2 - n1) + (m2 - m1) * (n2 - n1) - z * z * b * x0t0
                l1[2][3] = 0.25 * (m2 ** 4 - m1 ** 4) + (x0 ** 3) * (n2 - n1) + 2 * (m2 ** 2 - m1 ** 2) * (n2 - n1)
                else

                i = i + 1
            i = 1
            j = j + 1
            print()
