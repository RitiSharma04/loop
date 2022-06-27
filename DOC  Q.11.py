num=int(input("enter the num:-"))
count=0
while num>0:
    count=count+num%10
    num=num//10
print(count)    