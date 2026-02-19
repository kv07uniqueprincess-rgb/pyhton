print("enter five marks:")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
tot=m1+m2+m3+m4+m5
avg=tot/5
if m1>34 and m2>34 and m3>34 and m4>34 and m5>34:
 res="pass"
else:
 res="fail"
if res=="pass":
 if avg>=85:
    gra="outstanding"
 if avg>=75:
    gra="excellent"
 elif avg>=65:
    gra="very good"
 elif avg>=55:
    gra="good"
 else:
    gra="fair"
else:
    gra="no grade because fail"
print("total mark:",tot)
print("average mark:",avg)
print("result:",res)
print("grade",gra)
                
        
    
