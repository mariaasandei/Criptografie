def euclid_extins(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = euclid_extins(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# Exemplu de utilizare:
a, b = 35, 15
rezultat, x, y = euclid_extins(a, b)
print(f"GCD: {rezultat}, x: {x}, y: {y}")