i=0
while i<=4:
    j=0
    while j<=4:
        if i==j or i==4 or j==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")    
        j=j+1
    print()
    i=i+1        