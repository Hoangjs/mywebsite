def check(A,a):
    c=0
    b=0
    while c < len(A):
        if A[c]=='X':
            b+=1
            c+=a
        else:
            c+=a
    return b
with open ("VOTE.inp","r")as f:
    data=f.readlines()
    a=int(data[0])
    C=[]
    B=[]
    L=[]
    n=1
    t=0
    l=0
    for i in range (1,a+1):
        A=list(map(str,(data[i].split())))
        for k in A:
            B.append(k)
    while l<a:
        C.append(check(B,a))
        B.remove(B[0])
        l+=1
    for i in C:
        if i== max(C) :
            L.append(n)
            n+=1
            t+=1
        else :
            n+=1
    kq3=" ".join(map(str,L))
with open ("VOTE.out","w")as f:
    f.writelines(str(t)+" "+str(max(C))+"\n"+kq3)