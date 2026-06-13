# i=0
# list_1=[1,20,"hello",True,"Chomu",80,50.4,810,"sassy","sorry"]
# for i in list_1:
#     print(i,end=" ")
# for i in range(len(list_1)):
#     i+=1
# print("The number of elements in the list are :- ",i)

# list_1= [1,10,100,3,6,8]
# list_1.insert(2,59)
# print(list_1)

# list_1=[1,2,3,4,5,6,7,8,9,10]
# print(list_1[1::2])

# list_1= ["Gaurav",12,23,33.33,"Sharma",True]
# for i in list_1:
#     if i==str(i):
#         print(i)

# list_1=["Gaurav",12,23,33.33,"Sharma",True]
# sum=0
# for i in list_1:
#     if type(i)==int or type(i)==float:
#         sum+=i
# print("The sum of the given numbers are :- ",sum)

# list_1=[]
# while True:
#     a=input("Enter the element which u want to add in the list :- ")
#     if a=="-1":
#         break
#     elif a.isnumeric():
#         list_1.append(int(a))
#     else:
#         list_1.append(a)
# print(list_1)


# list_1=[1,2,3,4,5]

# while True:
#     a=input("Enter 0 for new friend or -1 to stop or 1 for important friend or 2 for printing the list :- ")
#     if a=="-1":
#         break
#     elif a=="1":
#         b=int(input("Enter the index of the new friend if your friend is important:- "))
#         new_friend=input("Enter your boyfriend name :- ")
#         list_1.insert(b,new_friend)
#     elif a=="0":
#         friend_name=input("Enter your friend name :- ")
#         list_1.append(friend_name)
#     elif a=="2":
#         print("Your elements in the list are :- \n",list_1)
#     else:
#         print("You have chosen some wrong number.")


li1=[i for i in range(5)]
print(li1)