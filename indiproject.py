import datetime

class employee:

   
    def __init__(self,name=None,age=None,phone=None,add=None,dateOfRegistration=None,insurance=None,disability=None, diplomat=None,gender=None,status=None,income=None,yearly_income=None,tax_amount=None):
        self.name = name
        self.age = age
        self.phone = phone
        self.add = add
        self.dateOfRegistration= dateOfRegistration
        self.insurance = insurance
        self.disability = disability
        self.diplomat = diplomat
        self.income= income
        self.gender = gender
        self.status = status 
        self.yearly_income = yearly_income
        self.tax_amount = tax_amount

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getPhone(self):
        return self.phone       
    def getStatus(self):
        return self.status
    def getAddress(self):
        return self.add
    def getIncome(self):
        return self.income
    def getGender(self):
        return self.gender
    def getyearly_income(self):
        return self.yearly_income

    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def setStatus(self,status):
        self.status = status
    def setAddress(self,address):
        self.add = address
    def setIncome(self,income):
        self.income = income
    def setyearly_income(self,yearly_income):
        self.yearly_income = yearly_income
        



    def staticInfo(self):
        print("\t\t\t\tIncome Tax Calculation System")
        print("\t\t\t\t\tLazimpart,Kathmandu")
        print("--------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tWelcome to the Income Tax Calculation System")
        print("\t\t\t\t\t\t\t\t\tDate:",datetime.datetime.now())
        print("--------------------------------------------------------------------------------------------------------------")        

    def EmployeeInformation(self):

        self.name =input("Enter Your Name::")
        self.add=input("Enter Your address::")
        self.age=int(input("Enter Your Age::"))
        self.phone = input("Enter phone number :")
        self.status=input("Are you married or unmarried(m/u)::")
        self.dateOfRegistration = datetime.date.today()
        self.insurance = input("have you done insurance?(y/n)")
        self.disability = input("do you have a disability?(y/n)")
        self.diplomat = input("are you a diplomat?(y/n)")
        self.gender = input("what is your gender?(m/w)")
        print("---------------------")
        self.income=int(input("Enter the Monthly income::"))
        self.yearly_income=self.income*12
        print("Your Yearly income is", self.yearly_income)
        

    def CalculateInsurance(self):
        if self.insurance == "y":
            self.yearly_income = self.yearly_income-20000
        

        
    def CalculateCouple(self):
        self.CalculateInsurance()
        if(self.yearly_income<450000):
            self.tax_amount=self.yearly_income*0.01
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=450000 or self.yearly_income<550000):
            self.tax_amount=4500+((self.yearly_income-400000)*0.1)
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=550000 and self.yearly_income<750000):
            self.tax_amount=14500+((self.yearly_income-500000)*0.2)
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=750000 and self.yearly_income<2000000):
            self.tax_amount=54500+((self.yearly_income-700000)*0.3)
            print("Your taxable amount is",self.tax_amount)
        else:
            self.tax_amount=429500+((self.yearly_income-2000000)*0.36)
            print("Your taxable amount is",self.tax_amount)
        
        self.getDiplomat
        self.getDisability
        self.getGender
        


    def CalculateIndividual(self):
        self.CalculateInsurance()
        if(self.yearly_income<400000):
            self.tax_amount=self.yearly_income*0.01
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=400000 or self.yearly_income<500000):
            self.tax_amount=4000+((self.yearly_income-400000)*0.1)
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=500000 and self.yearly_income<700000):
            self.tax_amount=14000+((self.yearly_income-500000)*0.2)
            print("Your taxable amount is",self.tax_amount)
        elif(self.yearly_income>=700000 and self.yearly_income<2000000):
            self.tax_amount=54000+((self.yearly_income-700000)*0.3)
            print("Your taxable amount is",self.tax_amount)
        else:
            self.tax_amount=444000+((self.yearly_income-2000000)*0.36)
            print("Your taxable amount is",self.tax_amount)
        self.getDiplomat
        self.getDisability
        self.getGender

    def getDisability(self):
        if(self.disability == 'y'):
            self.tax_amount = self.tax_amount - self.tax_amount*.5
            if(self.gender == 'w'):
                self.tax_amount = self.tax_amount - self.tax_amount*.1
        return self.tax_amount
        
        

    def getDiplomat(self):
        if(self.diplomat == 'y'):
            self.tax_amount = self.tax_amount - self.tax_amount*.75
            if(self.disability=='n'):
                if(self.gender == 'w'):
                    self.tax_amount = self.tax_amount - self.tax_amount*.1
        return self.diplomat
    
    def getGender(self):
        if(self.diplomat == 'n'):
            if(self.disability=='n'):
                if(self.gender == 'w'):
                    self.tax_amount = self.tax_amount - self.tax_amount*.1
        return self.diplomat

    def DisplayOutput(self):
        f = open("demofile.txt", "w")
        f.write("-------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\t\t\t\tIncome Tax Calculation System\n")
        f.write("\t\t\t\t\t\t\t\t\tLazimpart,Kathmandu\n")
        f.write("--------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\t\tWelcome to the Income Tax Calculation System\n")
        f.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tData:")
        f.write(str(datetime.datetime.now()))
        f.write("\n--------------------------------------------------------------------------------------------------------------\n")
        f.write("Employee Details::\n")
        L = ["Name::",self.name,"\t\t\t\t\t\t\t\tAddress::",self.add,"\n"]
        f.writelines(L)
        M = ["Age::",str(self.age),"\t\t\t\t\t\t\t\t\tMaritial Status::",self.status,"\n"]
        f.writelines(M)
        k = ["Date of registration::",str(self.dateOfRegistration)]
        f.writelines(k)
        f.write("(Note:: m=married and u=unmarried)\n")
        N = ["Monthly income::",str(self.income),"\t\t\t\t\t\t\t\tYearly income::",str(self.yearly_income),"\n"]
        f.writelines(N)
        T = ["Your taxable amount is ",str(self.tax_amount),"\n"]
        f.writelines(T)
        f.close()

def main():
    cust = employee()
    
    cust.staticInfo()
    cust.EmployeeInformation()
   
    if(cust.status == "m"):
        cust.CalculateCouple()
    else:
        cust.CalculateIndividual()
    cust.DisplayOutput()
        
    

main()

