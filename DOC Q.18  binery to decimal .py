a=int(input("enter the number:-"))
sum=0
i=0
while a>0:
    sum=sum+(a%10)*(2**i)
    a=a//10
    i=i+1
print(sum)    