# a=int(input("enter the a"))
# i=1
# while i<=a:
#     if a//10==1:
#         print("one")
#     elif a//10==2:
#         print("two")
#     elif a//10==3:
#         print("three")
#     a=a%10  
#     i=i+1  
s=5
i=1
while i<=5:
    j=1
    while j<=5:
        if j<i:
            print(i,end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    s=s+1
    i=i+1        