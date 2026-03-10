def euler_phi(n):
    rezultat = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            rezultat -= rezultat // p
        p += 1

    if n > 1:
        rezultat -= rezultat // n

    return rezultat


# Exemplu pentru un nr mare
numar = 123456789
print(f"phi({numar}) = {euler_phi(numar)}")