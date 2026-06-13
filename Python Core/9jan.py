# a="Hello world"
# for i in (a):
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         print(i)

# count=0
# a_count=0
# e_count=0
# i_count=0
# o_count=0
# u_count=0
# string=input("Enter the string :- ")
# for i in string:
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         print(i,end=" ")
#         count+=1
#     if (i=="a"):            
#         a_count+=1
#     if (i=="e"):            
#         e_count+=1
#     if (i=="i"):            
#         i_count+=1
#     if (i=="o"):            
#         o_count+=1
#     if (i=="o"):            
#         u_count+=1
# print("The number of vowels in this is :- ",count)
# print("The number of \"A\" repeated here is :- ",a_count)
# print("The number of \"E\" repeated here is :- ",e_count)
# print("The number of \"I\" repeated here is :- ",i_count)
# print("The number of \"O\" repeated here is :- ",o_count)
# print("The number of \"U\" repeated here is :- ",u_count)

# count=0
# string=input("Enter the whole string :- ")
# string_find=input("Enter the string you want to find :- ")
# place=int(input("Enter the place :- "))
# for i in range(len(string)):
#     if string[i]==string_find:
#         count+=1
#         if count==place:
#             print("Your required character from the whole string is at the ",i+1,"th place.")


# string= "India is a country in asia where we all live"
# find_string=input("Enter the character which you want to find :- ")
# print(string.rfind("i"))



# sum=0
# num_sum=0
# string=input("Enter the whole string :- ")
# print("The total character in this string is :- ",len(string))
# string_remove_spaced=string.replace(" ","")
# print("The length of the string after removing the space :- ",string_remove_spaced)
# for i in string:
#     if i=="a":
#         sum=sum+1
# print("Numbers of times \"A\" repeated here is :- ",sum)

# for i in string:
#     if i.isdigit():
#         num_sum+=1
# print("The number of digits here is :- ",num_sum)



# a = "hhgfskh 23423 43r kjdsbf 3434 hb 342 hh234 324 kjebf"
# for i in a:
#     if i.isdigit():
#         print(i, end="")
#     if i.isspace():
        # print("")

# a=int(input("Enter the first number :- "))
# b=int(input("Enter the first number :- "))
# c=int(input("Enter the first number :- "))
# if (a>b) and (a>c):
#     print("The first number is greater than second and third.")
# elif (b>a) and (b>c):
#     print("The second number is greater than first and third.")
# elif (a==b) and (a>c):
#     print("The first number is equal to second number but third is smaller than that.")
# else:
#     print("The third number is greater than first and second.")


# number=int(input("Enter the number :- "))
# if number%10==0 and number%3==0 and number%5==0:
#     print("The number is fully divisible by 10, 5 and 3.")