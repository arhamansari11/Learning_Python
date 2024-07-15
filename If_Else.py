gender = input("Enter your Gender : ")

if gender == "Male":
    salary = int(input("Enter your salary : "))
    if salary >= 30000:
        print("You are eligible for loan")
    else:
        print("You are not Eligible for loan")
elif gender == "Female":
    salary = int(input("Enter your Salary : "))
    if salary >= 20000:
        print("You are Eligible for loan")
    else:
        print("You are not Eligible for loan")
else:
    print("Check your Gender Please")