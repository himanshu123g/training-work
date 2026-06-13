# colour_name=["Black", "Red", "Maroon", "Yellow"]
# colour_codes=["#000000", "#FF0000", "#800000", "#FFFF00"]
# result = []
# d = {}

# for i,j in zip(colour_name,colour_codes):
#     d={}
#     d["color_nam"] = i
#     d["color_code"] = j
#     result.append(d)
# print(result)


dic={"name":"shubham",
     "age":22,
     80:"marks",
     "gender":"male",True:"boy","name":"Aman"}

# print(dic)

# dic.pop("name")
# print(dic)
# print(dic.items())
# print(dic.keys())
# print(dic.values())
# print(type(dic))
# print(type(dic["age"]))

dic={"name":"shubham",
     "age":22,
     80:"marks",
     "gender":"male",True:"boy","name":"Aman",
     "movie":2012}

# for i in dic:
#     print(i,dic[i])

# for i, j in dic.items():
#     print(i,j)

# for i in dic.keys():
#     print(i)

# for i in dic.values():
#     print(i)

# for i in dic:
#     if type(dic[i])==int:
#         print(i,dic[i])

# a=int(input("Enter the number of items u wanna add:- "))
# dic={}
# for i in range(a):
#     key=input("Enter key :- ")
#     value=input("Enter value :- ")
#     dic[key]=value

#     if key.isalpha() and value.isalpha():
#         dic[key]=value
#     if key.isnumeric() and value.isnumeric():
#         (dic[int(key)])=int(value)
#     if key.isalpha() and value.isnumeric():
#         dic[key]=int(value)
#     if key.isnumeric() and value.isalpha():
#         (dic[int(key)])=value
# print(dic)


# d={"name":"Himanshu","age":20,"grade":"A"}
# print(d)

# q2={"name":"Himanshu","age":20,"grade":"A"}
# q2["Father"]="Rakesh"
# print(q2)

# fruits = {'apple': 5, 'banana': 3, 'orange': 7}
# for i,j in fruits.items():
#     print(i,j)

# d={}
# for i in range(1,6):
#     d[i]=(i*i)
# print(d)

company = {'dept1': {'name': 'IT', 'employees': 10},
                   'dept2': {'name': 'HR', 'employees': 5}}
print(company["dept2"]["name"])

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print(dict1.append(dict2))