#e=int(input("enter ending number:"))
#s=int(input("enter starting number:"))
#tot=0
#while e>=s:
   # print(e,end=" ")
    #tot=tot+e
   # e-=1
#print("Total:",tot)

#find vowels using while loop
name=input("Enter your text:")
vow="aeiou"
i=0
c=0
while i<len(name):
    if name[i] in vow:
        print(name[i],end=" ")
        c+=1
    i+=1
print("\nTotal no. of vowels:",c)
