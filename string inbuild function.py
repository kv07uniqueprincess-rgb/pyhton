#string inbuild function
k="karthikeyan"
print(type(k))
print(len(k))
print(k.capitalize())
print(k.title())
print(k.count("e"))

s="thejashree"
print(s.center(10)+".")
print(s.center(11)+".")
print(s.endswith("no"))
print(s.startswith("th"))
print(s.find("h"))
print(s.find("h",2))
print(s.index("h"))
print(s.index("h",2))
print(s.find("z"))
#print(s.index("z"))
s="123"
print(s.isalnum())
s="abc"
print(s.isalnum())
s="a@b$c"
print(s.isalnum())
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
s="\t\n\r\b"
print(s.isprintable())
s="gowtham!@#!#123113"
print(s.isprintable())
s=""

print(s.isspace()) #true
s="   a"
print(s.isspace())  #false
t="I Am So Good"
print(t.istitle())
t="I am viji comming from karur"

#t=t.title()
print(t)
print(t.istitle())
m="karur"
print(m.islower())
print(m.isupper())
k="jErcY"
print(k.swapcase())

#important:convert list to string
m=["mathi","azhagi","dhanu","viji","sano"]
print(type(m))
ans=",".join(m)
print(type(ans))
print(ans)

#important:convert string to list
t='kaviarasugo,kulpar,thobhankis,horemari,muthu'
print(type(t))
ans=t.split(" ")
print(type(ans))
print(ans)

n="sreesha"
ans=n.replace("r","o")
print(ans)
n="   viji   "
print(n.lstrip()+".")
print(n.rstrip()+".")
print(n.strip()+".")

amt="12345678"
print(amt.zfill(10)+"****")

#aadhar
aadhar="858415761049"
first=aadhar[:2]
last=aadhar[10:]
middle="********"
ans=first+middle+last
print("masked aadhar:",ans)


