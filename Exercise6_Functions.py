'''
#1. Sum of numbers
def sum_of_digits(x,y):
    sum=x+y
    return sum

a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
print(sum_of_digits(a,b))
'''
'''
#2.Prime finder
def prime_finder(y):
    cond=1
    for i in range(2,y):
        if y%i==0:
            cond=0
            break
    if cond==1:
        print(y)    

def separation(string):
    for x in string:
        z=int(x)
        prime_finder(z)

a=input("enter digits: ")
separation(a)
'''

'''
#3.odd+even
def find_sum_odd(a):
    sum=0
    for i in range(1,a+1):
        if i%2==0:
            sum=sum+i
    return sum

def find_sum_even(b):
    sum=0
    for i in range(1,b+1):
        if i%2!=0:
            sum=sum+i
    return sum

N=int(input("Enter number: "))
print(find_sum_odd(N))
print(find_sum_even(N))
'''
'''
def factors(a=1):
    for i in range(1,a+1):
        if a%i==0:
            print(i)

b=int(input("Enter number: "))
factors(b)
'''
'''
import math 

def sine_series(a,n):
    for i in (1,n+1):
        if i!=0:
            y=(((-1)**n)(a**i))/factorial(i)
            sum=sum+y
    return sum

n1=int(input("Enter number of terms: "))
b=int(input("Enter number: "))
print(sine_series(b,n1))
'''
'''
def rec_funct(n):

    if n!=0:
        return n*rec_funct(n-1)    
    else:
        return 1

a=int(input("Enter number"))
print("Factorial is ",rec_funct(a))
'''
'''
def fibonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return (fibonnaci(n-1)+fibonnaci(n-2))
    else:
        return 0

a=int(input("Enter a number: "))
for i in range(a):
    print(fibonnaci(i),end=" ")
'''
'''
def sum_of_digits(n):
    
    if n!=0:
        return n%10 + sum_of_digits(n//10)
        
    else:
        return 0
    
a=int(input("Enter number: "))
print(sum_of_digits(a))
'''
'''
def sum_of_positive(n):
    if n%2!=0:
        n-=1
    elif n<0:
        return 0
    else:
        return n+sum_of_positive(n-2)
    

a=int(input("Enter number: "))
print(sum_of_positive(a))
'''
'''
#GCD
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)
    '''
    

    

