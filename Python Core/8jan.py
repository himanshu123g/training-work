# i=0
# j=0
# for i in range(4):
#     for j in range(i+1):
#         print("*",end=" ")
#     print(" ")

# name=input("Enter your name :- ")
# value=int(input("Enter the number of times u want to print your name :- "))
# for i in range(value):
#     print("your name is ",name," and it is printed for the ",i+1," times.")

# number=int(input("Enter the number :- "))
# start_point=int(input("Enter the start point :- "))
# total_value=int(input("Enter the total value :- "))
# for i in range(start_point,total_value+start_point):
#     print(number,"x",i,"=",number*i)

# first_number=int(input("Enter first number :- "))
# second_number=int(input("Enter second number :- "))
# if (first_number<second_number):
#     print("AS THE FIRST NUMBER IS SMALLER THAN SECOND SO WE WILL PRINT A FORWARD LOOP.")
#     for i in range(first_number,second_number):
#         print(i+1,end=" ")
# else:
#     print("AS THE FIRST NUMBER IS GREATER THAN SECOND SO WE WILL PRINT A BACKWARD LOOP.")
#     for i in range (first_number,second_number,-1):
#         print(i,end=" ")


name=input("Enter your name :- ")
current_age=int(input("Enter your current age :- "))
current_year=int(input("Enter the current year :- "))
expected_year=int(input("Enter the expected year :- "))

for i in range (expected_year):
    print("Hey ",name," in ",current_year," you are ",current_age," old.")
    current_year+=1
    current_age+=1