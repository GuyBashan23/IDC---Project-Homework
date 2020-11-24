
n = 7
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is NOT a prime number")
           break
   else:
       print(n,"is a prime number")
else:
   print(n,"is NOT a prime number")

m=876
n=9
if not m==n:
    if m>n:
        lst=list(range(n,m))
    if m<n:
        lst=list(range(m,n))
    for elem in lst:
        if (elem%2)==0:
            lst.remove(elem)
    x=0
    for elen in lst:
        x=x+elen
    y=float(x/len(lst))
    print(y)
else: print(0.0)

p=5
for i in range(p,0,-1):
    for j in range(0,i):
        print(i, end="")
    print()


lst4 =  [0, 5.4, 0, 7, 6, 8.1, 3, 6, 0, 3]
for elem in lst4:
    if lst4.count(elem)>1:
        for elen in range(1,lst4.count(elem)):
            lst4.remove(elem)
print(lst4)


lst5 = ["hi", "ho", "ho", "ho", "no", 1, 1, "do", "you", "copy"]
x=len(lst5)
for elen in range(x):
    if elen<(x-1):
        if lst5[elen]==lst5[elen+1]:
            print(lst5[elen])
if x==0:
   print("No repetitions were found!")
            

