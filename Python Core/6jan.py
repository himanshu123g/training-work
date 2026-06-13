a=10
print(type(a))
print(float(a))


b=input("Enter the number :- ")
print(type(b))
b=int(b)
print(b**2)


print(type("3.14"))
c=float("3.14")
print(type(c))


d="3.5"
d=float(d)
d=int(d)
print(type(d))

e=input("Enter your name :- ")
f=input("Enter your age :- ")
print("Hello ",e ,"! You are ",f," years old.")


g=int(input("Enter the first number :- "))
h=int(input("Enter the second number :- "))
print("The sum of the given two numbers are :- ",g+h)


i=input("Enter first number :- ")
j=input("Enter second number :- ")
print(type(i))
print(type(j))
i=float(i)
j=float(j)
print(i*j)



k=int(input("Enter the temperature (in celcius) :- "))
print("The temperature in fahrenheit is :- ",(k*9/5)+32)


k=int(input("Enter the first number :- "))
l=int(input("Enter the second number :- "))
print("The sum of two numbers is :- ",k+l)
print("The subtraction of two numbers is :- ",k-l)
print("The multiplication of two numbers is :- ",k*l)
print("The division of two numbers is :- ",k/l)
print("The floor division of two numbers is :- ",k//l)
print("The exponential of two numbers is :- ",k**l)
print("The modulus of two numbers is :- ",k%l)



print(k==l)  #used to check if k is equal to l, will say true otherwise false
print(k>=l)  #used to check if k is greater than equal to l, will say true otherwise false
print(k<=l)  #used to check if k is less than equal to l, will say true otherwise false
print(k!=l)  #used to check if k is greater than equal to l, will say true otherwise false
print(k>l)   #used to check if k is greater than l, will say true otherwise false
print(k<l)   #used to check if k is less than l, will say true otherwise false


m=True
n=False
o=True
print(m and n)
print(m and m)
print(m or n)
print(not m)

p=60
q=50
print(p>q and p>=q)
print(p<q or p>=q)
print(not(p>q))

r=10
s=10
r+=3
print(r)
s-=4
print(s)


t=int(input("Enter the number to check if it is odd or even :- "))
if (t%2==0):
    print("The number is even.")
else:
    print("The number is odd.")