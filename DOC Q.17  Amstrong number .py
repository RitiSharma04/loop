a=int(input("enter the num:-"))
len=len(str(a))
sum=0
b=a
while a>0:
    sum+=(a%10)**len
    a=a//10
if sum==b:
    print("yes") 
else:
    print("no")       
