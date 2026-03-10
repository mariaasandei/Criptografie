import math

def fermat_factorizare(n):
    if n % 2 == 0:
        return 2, n // 2

    t = math.isqrt(n)

    if t * t == n:
        return t, t

    t += 1

    while True:
        s2 = t * t - n
        s = math.isqrt(s2)
        if s * s == s2:
            a = t - s
            b = t + s
            return a, b
        t += 1

n = int(input("Dati numarul n: "))

a, b = fermat_factorizare(n)

print(f"{n} = {a} x {b}")