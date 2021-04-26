#GIVEN CODE:
def factorial(n):
    if(n==0):
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(1,6):
    print("factorial of ",i,"is",factorial(i))

#MY CODE:
print("\nMY CODE ")
def factorial(n):
    if(n==0):
        return(1)                   #HERE I MADE A CHANGE
    else:
        return(n*factorial(n-1))
f=factorial(int(input("Enter the number :")))           #Here I made a change
print("factorial of the given number is :",f)