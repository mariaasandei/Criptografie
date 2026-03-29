import aux
mesaj="NOANSWER"
alfabet=aux.citeste_alfabet("alfabet.txt")
a=aux.Matrix([[2,3],[7,8]])
b=aux.Matrix([[0],[0]])
criptat=aux.criptare_Hill(mesaj,2,a,b,alfabet)
print(criptat)


#decriptare
criptare = aux.criptare_Hill(mesaj, 2, a, b, alfabet)
print(criptare)
N = len(alfabet)
a_prim = a.inv_mod(N)
b_prim = -a_prim * b
decriptare = aux.criptare_Hill(criptare, 2, a_prim, b_prim, alfabet)
print(decriptare)
