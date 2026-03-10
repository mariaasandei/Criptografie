import math

def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def f(x, c, n):
    return (x * x + c) % n

def pollard_rho(n):
    if n % 2 == 0:
        return 2, n // 2

    x = 2
    y = 2
    c = 1
    d = 1

    while d == 1:
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        d = cmmdc(abs(x - y), n)

    return d, n // d

n = int(input("Dati numarul n: "))

a, b = pollard_rho(n)

print(f"{n} = {a} x {b}")