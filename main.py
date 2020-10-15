num=int(input())
x, y, z = [int(x) for x in input().split(" ")]
a, b, c = [int(a) for a in input().split(" ")]
win=0
m=a
n=b
o=c
p=x
q=y
r=z
lose=0
while(x!=0 and b!=0):
    while(b!=0):
        x-=1
        win+=1
        b-=1
        if(x==0):
            break
while(y!=0 and c!=0):
    while(c!=0):
        y-=1
        c-=1
        win+=1
        if(y==0):
            break
        
while(z!=0 and a!=0):
    while(a!=0):
        z-=1
        a-=1
        win+=1
        if(z==0):
            break
while(p!=0 and o!=0):
    p-=1
    o-=1 

while(q!=0 and m!=0):
    q-=1
    m-=1

while(r!=0 and n!=0):
    r-=1
    n-=1 

while(p!=0 and m!=0):
    p-=1
    m-=1
while(q!=0 and n!=0):
    q-=1
    n-=1
while(r!=0 and o!=0):
    r-=1
    o-=1
print(str(p))
print(str(q))
print(str(r))
print(str(m))
print(str(n))
print(str(o))


print(str(lose)+" "+str(win))