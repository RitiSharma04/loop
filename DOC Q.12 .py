num=int(input("enter the num:-"))
pro=1
while num>0:
    b=num%10
    num=num//10
    pro*=b
print(pro)    

