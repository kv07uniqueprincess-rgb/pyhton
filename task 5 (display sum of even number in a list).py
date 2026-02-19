#for loop type:5 task
#display sum of even number in a list
k=[11,44,-55,66,77,12,-31,22,11,-10]
total=0
for i in k:
    if i%2==0:
        total+=i
        print("sum of even number",total)
