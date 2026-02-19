n=int(input("Enter size:"))
s=0
for i in range(n+1):
    s=s+i
    if i==n:
        print(i,end=" ")
    else:
        print(i,end="+")
print("=",s)
