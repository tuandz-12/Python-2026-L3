#Ex3
n = int(input("Enter a number:"))
def prime(n):
    if n<2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
if prime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")