
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(" WELCOME TO COLLAGE MANAGEMENT SYSTEM ")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

X=1

while(X>0):
    print("1.TO add student")
    print("2.To see student list")

    print("3.To remove student")

    print("4.to know student fee")

    print("5.To quit")

    A=['ram','vamsi','bai']


    a=int(input("enter choice:"))
    if(a==1):
        B=str(input("student name:"))

        father_name=input("father name:")

        mother_name=input("mother name:")

        student_addres=input("student addres:")

        phone_number=input("phone number:")

        DOB=input("DOB:")

        Board=input("10 Board:")

        Roll_no=input("10 Roll no :")

        Result=input("10 Result:")

        Blood_group=input("Blood group:")

        if(1>0):

            A.append(B)

            print("the student has been successfully added")

    elif(a==2):

        print(A)

    elif(a==3):

        C=str(input("enter name to remove:"))

        A.remove(C)

        print("the student has been successfully removed")

    elif(a==4):

        print("select 1 for Science stream")

        print("select 2 for Commerce Stream")

        G=int(input("Enter your choice:"))

        if G==1:

            print("")

            print("Science Stream")

            print("Adm. fees=80,000")

            print("Regestration fees=20,000")

            print("School funds=10,000")

            print("Technology fees=5000")

            print("Tuition fees=5000")

            print("Books=5000")

            print("Uniform=5000")

            print("Laboratory fees=3000")

            print("Picnic fees=2000")

            print("")

            print("TOTAL=1,35,000 INR")
        if(G==2):

            print("")

            print("Commerce Stream")

            print("Adm. fees=70,000")

            print("Regestration fees=20,000")

            print("School funds=10,000")

            print("Tuition fees=5000")

            print("Technology fees=5000")

            print("Books=3000")

            print("Uniform=5000")

            print("Picnic fees=2000")

            print("")

            print("TOTAL=1,20,000 INR")

    elif(a==5):

        print("Thank you")

        break




