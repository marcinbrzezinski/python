a = 4
b = 7


def extended_euclidean_alg(a, b):
    u = 1
    w = a
    x = 0
    z = b

    while w:
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q

        q = w // z
        u -= q * x
        w -= q * z

    if z == 1:
        if x < 0:
            x += b
        return x  # odwrotnosc z przedzialu [0, b - 1]
    else:
        return -1  # nie istnieje


print(extended_euclidean_alg(42, 2017))
