class multiplefunctions():
    def traingle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth"))
        areaoftraingle=(Height*Breadth)/2
        print("Area of formula: (Height*Breadth)/2")
        print("Area of Traingle:",areaoftraingle)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Height3=int(input("Height3:"))
        perimeteroftraingle=Height1+Height2+Height3
        print("perimeter of formula: Height1+Height2+Height3")
        print("perimeter of traingle:",perimeteroftraingle)
    
    def Eligible():
        Gender=input("Gender Name:")
        Age=int(input("Age:"))
        if(Gender=="Male" and Age>=21):
            print("ELIGIBLE")
        elif(Gender=="Female" and Age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
       subject1=int(input("subject1:"))
       subject2=int(input("subject2:"))
       subject3=int(input("subject3:"))
       subject4=int(input("subject4:"))
       subject5=int(input("subject5:"))
       total=subject1 + subject2 + subject3 + subject4 + subject5
       print("total=",total)
       Percentage=total/5
       print("Percentage=",Percentage)

    def subfields():
        word=['Sub-fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for i in word:
            print(i)
            
    def Oddeven():
        num=int(input("Enter the Number:"))
        if (num%2==0):
            print(num,"is the Even Number")
        else:
            print(num, "is the Odd Number")
        
            
        