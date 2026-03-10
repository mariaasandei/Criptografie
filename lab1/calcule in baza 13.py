def to_base_13(n):

    if n == 0:
        return "0"

    digits = "0123456789ABC"
    res = ""
    is_negative = n < 0
    n = abs(n)

    while n:
        res = digits[n % 13] + res
        n //= 13

    return "-" + res if is_negative else res


def calcule_baza_13(a_str, b_str, operatie):
    a_10 = int(a_str, 13)
    b_10 = int(b_str, 13)

    if operatie == '+':
        rezultat_10 = a_10 + b_10
    elif operatie == '-':
        rezultat_10 = a_10 - b_10
    elif operatie == '*':
        rezultat_10 = a_10 * b_10
    else:
        return "Operație invalidă"
    return to_base_13(rezultat_10)

numar1 = "A2"  # (10*13 + 2 = 132 în baza 10)
numar2 = "5"  # (5 în baza 10)

print(f"Adunare: {numar1} + {numar2} = {calcule_baza_13(numar1, numar2, '+')}")
print(f"Scădere: {numar1} - {numar2} = {calcule_baza_13(numar1, numar2, '-')}")
print(f"Înmulțire: {numar1} * {numar2} = {calcule_baza_13(numar1, numar2, '*')}")