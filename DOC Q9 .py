num1=int(input("enter the number1:-"))
num2=int(input("enter the number2:-"))
count=0
i=num1
while i<=num2:
    if i%2==0:
        count=count+i
    i=i+1
print(count)  