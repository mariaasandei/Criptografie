def citeste_alfabet(alfabet):
    with open(alfabet, "r", encoding="utf-8 ") as f:
        alfabet = f.read().strip()
    alfabet = tuple(alfabet)
    return alfabet

alfabet = citeste_alfabet("alfabet.txt")
print(alfabet)