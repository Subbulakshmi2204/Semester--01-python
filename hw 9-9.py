
n=int(input())
if n<2:
    f=False
else:
    f=True
    for i in range(2,n):
        if n%i==0:
            f=False
            break
        if f:
            print("Prime")
        else:
            print("Not prime")

num=int(input())
factorial=1
if num<0:
    print("No factorial for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print("The factorial of",num,"is",factorial)


n1=0
n2=1
count=0
if n<=0:
    print("Enter a positive integer")
elif n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1

n=int(input())
if n%11==0:
    print("Divisible by 11")
else:
    print("Not divisible")
    

num=int(input())
for i in range(1,num+1):
    if num%i==
        print(i,end=' ')
n=int(input())
