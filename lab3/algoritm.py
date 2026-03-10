import random
def a_la_b_mod_c(a,b,c):
    p=1
    a=a%c
    while b:
        if b%2==1:
            p=(p*a)%c
        a=(a*a)%c
        b//=2
    return p


def cmmdc(a, b):
     if a<0: a = -a
     if b<0: b = -b
     if a==0 or b==0: return a+b
     while (b):
        r = a%b; a = b; b = r
     return a

def test_Fermat(n, nr_incercari):
    if (n == 2): return True
    if (n % 2 == 0): return False
    for i in range(nr_incercari):
        b = random.randint(2, n - 2)
        if (cmmdc(b, n) != 1): return False
        if (a_la_b_mod_c(b, n - 1, n) != 1): return False
    return True

def test_Miller_Rabin(n, nr_incercari):
     if n == 2:
        return True
     if n < 2 or n % 2 == 0:
        return False
     for _ in range(nr_incercari):
         s = 0
         t = n - 1
         b = random.randint(2, n - 2)
         while t % 2 == 0:
             s += 1
             t //= 2
         t = a_la_b_mod_c(b, t, n)
         if t != 1:
             while t != n - 1 and s > 1:
                 t = (t * t) % n
                 s -= 1
                 if t == 1:
                     return False
                 if t!=n-1:
                     return False
     return True

print(test_Miller_Rabin(561,nr_incercari=10))

def test_Miller_Rabin2  (n,nr_incercari):
    if n%2==0:return True
    t=n-1;s=0
    while (t % 2) == 0: t=t//2;s=s+1
    for i in range(nr_incercari):
        b = random.randint(2, n - 2)
        if (cmmdc(b, n) != 1): return False
        p=a_la_b_mod_c(b, t, n)
        if p==1:continue
        x=s;
        while s>0:
            if p==n-1:break
            if p==1: return False
            p=(p*p)%n
            s-=1;
        if p!=n-1:return False
    return True
print(test_Miller_Rabin2(561,nr_incercari=1))

#print(test_Fermat(97,2))
#print(test_Fermat(561,2))
n = int(input("alege un nr:"))
#nr_incercari = int(input("Dati numarul de incercari:"))
#if (test_Fermat(n, nr_incercari)):
 #print(f"\nNumarul {n} poate fi prim")
#else:
 #print(f"\nNumarul {n} poate fi prim")
#print("Alege un numar: ")
print("Felicitari , ai luat licenta")