age=int(input("enter your age:"))
gender=input("enter gender:")
if gender=="female":
    if age>21:
        print("eilgible to marriage")
    else:
        print("not eilgible to marriage")
elif gender=="male":
    if age>23:
        print("eilgible to marriage")
    else:
        print("not eilgible to marriage")
else:
        print("invalid gender")
