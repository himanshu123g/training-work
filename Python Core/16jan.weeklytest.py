student_data = {
    "student_1": [2,2,2,2,1], #should lie between 0 to 10 and grade is E
    "student_2": [3,3,3,3,3],  #should lie between 11 to 20 and grade is D
    "student_3": [4,4,4,4,8], #should lie between 21 to 30 and grade is C
    "student_4": [10,10,5,5,5], #should lie between 31 to 40 and grade is B
    "student_5": [10,10,10,10,9]  #should lie between 41 to 50 and grade is A.
}
result={}
sum=0
for i in student_data:
    sum=0
    print(i,student_data[i])  #will used for accessing the key and the values of all.
    for j in student_data[i]:
        sum=sum+j
    
    if sum>=41 and sum<=50:
        grade = "A"
    elif sum>=31 and sum<=40:
        grade = "B"
    elif sum>=21 and sum<=30:
        grade = "C"
    elif sum>=11 and sum<=20:
        grade = "D"
    elif sum>=0 and sum<=10:
        grade = "E"
    else:
        print("Invalid Result.")
    result[i]={"total Marks :- " :sum, "Grade :- ":grade }

print(result)


