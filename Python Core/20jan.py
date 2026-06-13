# a=int(input("Enter the number :- "))
# b=int(input("Enter the number :- "))
# try:
#     ("The result of a/b is :- ",a/b)
# except:
#     print("This is the error.")


with open("abc.txt","r") as f:
    print(f.read())

with open("abc.txt","w") as f:
    f.write("hello ji , harsh mai satvik ki mummy")
    f.close()

with open("abc.txt","r") as f:
    print(f.read())