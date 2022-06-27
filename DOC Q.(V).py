# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()    
# def merge_the_tools(string, k):
#     # your code goes here
#      for i in range(0,len(string), k):
#         #slice string upto k characters
#         line = string[i:i+k]
#         seen = set()
#         for i in line:
#             #only print if we haven't already seen this character
#             if i not in seen:
#                 print(i,end="")
#                 seen.add(i)
#         #prints a new line
#         print()
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# n = int(input().strip())
# if n%2!=0:
#         print("Weird")
# elif n%2==0 and n>=2 and n<=5:
#             print("Not Weird")
# elif n%2==0 and n>=6 and n<=20:
#             print("Weird")
# elif n%2==0 and n>20:          
#         print("Not Weird")


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
    

year = int(input())
print(is_leap(year))

