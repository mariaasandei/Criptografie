import random

def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def a_la_b_mod_c(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result

def jacobi(b, n):
    b = b % n
    result = 1
    while b != 0:
        while b % 2 == 0:
            b //= 2
            if n % 8 in [3, 5]:
                result = -result
        b, n = n, b
        if b % 4 == 3 and n % 4 == 3:
            result = -result
        b = b % n
    if n == 1:
        return result
    return 0

def solovay_strassen(n, nr_incercari):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for _ in range(nr_incercari):
        b = random.randint(2, n - 1)
        if cmmdc(b, n) != 1:
            return False
        j = jacobi(b, n) % n
        e = a_la_b_mod_c(b, (n - 1) // 2, n)
        if e != j:
            return False
    return True

n = int(input("Dati numarul n: "))
nr_incercari = int(input("Dati numarul de incercari: "))

if solovay_strassen(n, nr_incercari):
    print(f"Numarul {n} poate fi prim")
else:
    print(f"Numarul {n} nu este prim")