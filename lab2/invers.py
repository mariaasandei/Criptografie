def invers(a,b):
    if a<0:a=-a
    if b<0:b=-b
    #if a==0 or b==0:return a+b
    xa=1;xb=0;copy=b;
    while b:
        r=a%b;
        xr=xa-(a//b)*xb
        a=b;b=r
        xa=xb;xb=xr;
    if (a == 1): return xa%copy;
    return None
print(invers(122,343))


