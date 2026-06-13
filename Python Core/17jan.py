# def temp():
#     temp=int(input("Enter the temperature in celcius :- "))
#     print("Your temperature from celcius to fahrenheit is :- ",(9/5*temp)+32)
# temp()


# import math as m
# def gcd(num_1,num_2):
#     print(m.gcd(num_1,num_2))
# gcd(15,20)


# def merged_list(a,b):
#     merged_list=a+b
#     merged_list.sort()
#     print(merged_list)
# a=[1,9,5]
# b=[15,25,2]
# merged_list(a,b)


# def vowel_count():
#     string=input("Enter the string here :- ")
#     sum_count=0
#     for i in string:
#         if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
#             sum_count=sum_count+1
#     print(sum_count)
# vowel_count()


# def highest():
#     list=[]
#     num=int(input("Enter the elements you wanna add into the list :- "))
#     for i in range(num):
#         value=int(input("Enter the value :- "))
#         list.append(value)
#     print("Your value in the list are :- ",list)
#     list.sort()
#     print("The second highest elements in this list is :- ",list[-2])
# highest()


# def remove_dup():
#     unique_list=[]
#     list=[]
#     num=int(input("Enter the elements you wanna add into the list :- "))
#     for i in range(num):
#         value=int(input("Enter the value :- "))
#         list.append(value)
#     print("Your value in the list are :- ",list)
#     for i in list:
#         if i not in unique_list:
#             unique_list.append(i)
#     print(unique_list)
# remove_dup()

# def dead_numbers():
#     dead_number=int(input("Enter the dead number :- "))
#     for i in range(2,dead_number):
#         if dead_number%i==0:
#             flag=0
#             break
#         else:
#             flag=1
#     if flag==0:
#         print("Not Prime.")
#     else:
#         print("Prime.")
# dead_numbers()

# def year(year):
#     leap=1
#     if year % 400 == 0:
#         print("This year is leap year.")
#     elif year % 100 == 0:
#         print("This year is not leap year.")
#     elif year % 4 == 0:
#         print("This year is leap year.")
#     else:
#         print("This year is not leap year.")
# year(1000)

# def string(x):
#     split_s=x.split()
#     words=split_s[::-1]
#     join_j=" ".join(words)
#     print(join_j)

# string("hello how are you")