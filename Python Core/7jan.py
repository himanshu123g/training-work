month_name=input("Enter the number you want to know the month name :- ")
if (month_name=="1"):
    print("The month is first and name of the month is January.")
elif (month_name=="2"):
    print("The month is second and name of the month is February.")
elif (month_name=="3"):
    print("The month is third and name of the month is march.")
elif (month_name=="4"):
    print("The month is fourth and name of the month is april.")
elif (month_name=="5"):
    print("The month is fifth and name of the month is may.")
elif (month_name=="6"):
    print("The month is sixth and name of the month is june.")
elif (month_name=="7"):
    print("The month is seventh and name of the month is july.")
elif (month_name=="8"):
    print("The month is eighth and name of the month is august.")
elif (month_name=="9"):
    print("The month is nineth and name of the month is september.")
elif (month_name=="10"):
    print("The month is tenth and name of the month is october.")
elif (month_name=="11"):
    print("The month is eleventh and name of the month is november.")
elif (month_name=="12"):
    print("The month is twelth and name of the month is december.")
else:
    print("Please put valid number as month only exist between 1 to 12.")


number_1=int(input("Enter the first number :- "))
number_2=int(input("Enter the second number :- "))

if (number_1==number_2):
    print("Numbers are equal.")
else:
    print("Numbers are not equal.")
    if (number_1>number_2):  
        print(number_1," is greater than ",number_2)
        print("Printing the first name five times according to the condition :- ")
        for i in range(1,6):
            print("Himanshu")
    else:
        print(number_2," is greater than ",number_1)
        print("Printing your last name three times as according to the condition.")
        for i in range(1,4):
            print("Sodhi.")


string_1=input("Enter your first string :- ")
string_2=input("Enter your second string :- ")
if string_1 is string_2:
    print("String 1 is equal to string 2.")
else:
    print("String 1 and string 2 are not equal.")

if (string_1 == string_2):
    print("String 1 is equal to string 2.")
else:
    print("String 1 and string 2 are not equal.")

d="3.5"
d=float(d)
d=int(d)
print(type(d))

e="3.5"
e=float(e)
e=int(e)
print(type(e))

print("The result of the two integers are :- ",d+e)



budget=int(input("Enter your budget (Your budget should rely between 2500$ to 10,000$) :- "))

if (budget>=2500 and budget<=3000):
    print("Your can visit Dubai.")
    places_dubai=int(input("Do you also want to know about the places in dubai? (Press 1 for yes and press 0 for No) :- "))
    if (places_dubai==1):
        print("The following places you can visit in Dubai :- \n Burj Khalifa \n Museum of the Future \n Burj Al Arab \n Dubai Fountain")
    elif (places_dubai==0):
        print("It was a great time to help you.")
    else:
        print("Please run the code again as we told you to choose the number only 1 and 0.")

elif (budget>3000 and budget<=6000):
    print("You can visit German.")
    places_german=int(input("Do you also want to know about the places in German? (Press 1 for yes and press 0 for No) :- "))
    if (places_german==1):
        print("The following places you can visit in German :- \n Berlin\n Hamburg\n Munich")
    elif (places_german==0):
        print("It was a great time to help you.")
    else:
        print("Please run the code again as we told you to choose the number only 1 and 0.")

elif (budget>6000 and budget<=9000):
    print("You can visit Australia.")
    places_australia=int(input("Do you also want to know about the places in Australia? (Press 1 for yes and press 0 for No) :- "))
    if (places_australia==1):
        print("The following places you can visit in Australia :- \n Sydney\n Melbourne\n Brisbane \n Gold Coast")
    elif (places_australia==0):
        print("It was a great time to help you.")
    else:
        print("Please run the code again as we told you to choose the number only 1 and 0.")

elif (budget>9000 and budget<=10000):
    print("You will visit Canada.")
    places_canada=int(input("Do you also want to know about the places in Canada? (Press 1 for yes and press 0 for No) :- "))
    if (places_canada==1):
        print("The following places you can visit in Canada :- \n Toronto\n Vancouver\n Montreal\n Quebec City")
    elif (places_canada==0):
        print("It was a great time to help you.")
    else:
        print("Please run the code again as we told you to choose the number only 1 and 0.")

else:
    print("you are going out of the conditions. Please check your values.")