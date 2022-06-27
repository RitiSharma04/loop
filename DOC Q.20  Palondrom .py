a=int(input("enter the number:-"))
rev=0
s=a
while a>0:
    rev=(rev*10)+a%10
    a=a//10
if s==rev:
    print("yes")
else:
    print("no")        


