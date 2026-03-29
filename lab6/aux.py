from sympy import Matrix
from collections import Counter


def citeste_alfabet(fisier_alfabet):
     with open(fisier_alfabet, "r", encoding="utf-8 ") as f:
         alfabet = f.read().strip()
     alfabet = tuple(alfabet)
     return alfabet

def get_text(fisier_sursa):
     with open(fisier_sursa, "r", encoding="utf-8") as f:
        text = f.read()
     return text

def write_text(fisier_destinatie, text):
     with open(fisier_destinatie, "w", encoding="utf-8") as f:
        f.write(text)

def cesar_encrypt(text,k,alfabet):
    N=len(alfabet)
    res=""
    for ch in text:
        res+=alfabet[(alfabet.index(ch)+k)%N]
    return res

def affine_encrypt(text,a,b,alfabet):
    N=len(alfabet)
    res=""
    for ch in text:
        res+=alfabet[(alfabet.index(ch)*a+b)%N]
    return res

def invers(a, N):
    x1 = 1
    x2 = 0
    copy = N

    while N:
        r = a % N
        x = x1 - (a // N) * x2
        x1 = x2
        x2 = x
        a = N
        N = r

    if a == 1:
        return x1 % copy
    return None


def get_frequencies(text):
    res=Counter()
    for ch in text:
        res[ch]+=1
    return res.most_common()

def criptare_Hill(text, n, a, b, alfabet):
    N = len(alfabet)
    char_to_index = {c: i for i, c in enumerate(alfabet)}
    if len(text) % n != 0:
        text += alfabet[0] * (n - len(text) % n)
    rezultat = ""
    for j in range(0, len(text), n):
        bloc = text[j:j + n]
        mesaj = Matrix([char_to_index[c] for c in bloc])
        criptat = (a * mesaj + b) % N
        for c in criptat:
            rezultat+=alfabet[int(c)]
    return rezultat
