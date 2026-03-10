def a_la_b_mod_c(a,b,c):
    p=1
    a=a%c
    while b:
        if b%2==1:
            p=(p*a)%c
        a=(a*a)%c
        b//=2
    return p
print(a_la_b_mod_c(a=2,b=40,c=105))