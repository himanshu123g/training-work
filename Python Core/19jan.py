# x= lambda a,b:(a+b)
# print(x(30,20))

# hello= lambda m,n:(m*n)
# print(hello(20,50))

# y=lambda a: True if a>50 else False
# print(y(60))

# def double(x):
#     return x*2
# a=[1,2,3,4,5,6,7,8,9]
# b=map(double,a)
# print(list(b))

# a=map(lambda x:x*2,[1,2,3,4,5,6,7,8,9])
# print(list(a))


# def e_o (x):
#     if x%2==0:
#         print("Even")
#     else:
#         print("Odd")
# b=map(e_o,[1,2,3,4,5,6,7,8,9])
# print(list(e_o,b))

# b=map(lambda oddeven:"even" if oddeven%2==0 else "odd.",[30,20,10,5,3])
# print(list(b))

# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# def even(x):
#     return x%2==0

# l=[1,2,3,4,5,6]
# a=map(even,l)
# print(list(a))

a=filter(lambda fil:fil in "AEIOUaeiou","hello how are you")
print(list(a))

