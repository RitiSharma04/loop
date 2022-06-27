a=input("enter the num")
i=1
count=0
while i<=len(a):
    if int(a[-i])==1:
        count=count+(2**i)*int(a[-i])
    i=i+1
print(count)        