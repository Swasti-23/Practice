#Q2 Sandglass pattern
n=int(input("Enter a number:"))
for i in range(n):
   print(" "*i,end="")
   print("* "*(n-i),end="")
   print()
for i in range(n-1):
    print(" "*(5-i-2),end="")
    print("* "*(i+2),end="")
    print()