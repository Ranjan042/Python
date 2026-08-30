n=int(input("Enter the No. of terms"))

def sumfunction(n):
    if(n==0):
     return 0
    else:
        return n+sumfunction(n-1)

ans=sumfunction(n)
print(f"sum of all natural number from 1 to {n}= {ans}")