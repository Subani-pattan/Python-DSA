''''class Mobile:
    def __init__(self,brand,price,color):
        print("Mobile objecct is created..")
        self.brand=brand
        self.price=price
        self.color=color
def details(self):
    print("----------------")
    print(f"brand is {self.brand} ")
    print(f"price is {self.price}")
    print(f"color is {self.color}")
b1=Mobile('iphone',50000,'black')
details(b1)
b2=Mobile('redmi',20000,'blue')
details(b2)
b3=Mobile('oppo',30000,'green')
details(b3)        
b4=Mobile('realme',45000,'mat black')
details(b4)
b5=Mobile('infinix',55000,'pale blue')
details(b5)


class Customer:
    def __init__(self):
        pass
def set_name(self,name):
    self.name=name
def  set_age(self,age):
    self.age=age
def set_id(self,id):
    self.id=id

def get_name(self):
    print(f"name is {self.name}")
def get_age(self):
    print(f"age is {self.age}")
def get_id(self):
    print(f"id is {self.id}")
c1=Customer()

class Std():
    @classmethod
    def show_data(cls):
        print("subani")
subani= Std()
Std.show_data()


class Mobile():
    @staticmethod
    def show_model():
        print("iphone 13")
iphone = Mobile()
Mobile.show_model()'''


'''class Vehicle():
    def __init__(self,b,p,c,s):
        self.b=b
        self.p=p
        self.c=c
        self.s=s
        print("Vehicle class constructor")
class Bike(Vehicle):
    def __init__(self, b, p, c, s,g,m):
        super().__init__(b, p, c, s)
        self.g=g
        self.m=m
        print("Bike class constructor")
b1 = Bike('tata',25000,'dark brown',2,3,56)


class Employee:
    def __init__(self):
        pass
    def work_hours(self):
        print("Employee works 8 hours a day ")
class Intern(Employee):
    def __init__(self):
        super().__init__()
    def work_hours(self):
        print("Interns works 6 hours a day")
s = Intern()
s.work_hours()
d = Employee()
d.work_hours()


class Vehicle1:
    def __init__(self):
        print("vehicle1 class created...")
class Vehicle2:
    def __init__(self):
        print("vehicle2 class created...")
class c:
    def __init__(self):
        print("vehicle1 and vehicle2")
C= c()
d= Vehicle1()
r= Vehicle2()

class Bankacct:
    def __init__(self,name,accno,pin):
        self.__name=name
        self.__accno=accno
        self.__pin=pin
        print("Bank acct is created")
    def subbu_name(self):
        print(self.__name)
    def subbu_accno(self):
        print(self.__accno)
    def subbu_pin(self):
        print(self.__pin)
b1=Bankacct('uday',23456789,2324)
b1.subbu_name()
b1.subbu_accno()
b1.subbu_pin()

class Candidate:
    def __init__(self,name,skills):
        pass
class Job_opening:
    def __init__(self):
        print()
class Interview:
    def __init__(self):
        print()
class RecuAi

class Employee:
    def __init__(self):
        pass
    def work_hours(self):
        return 
class Intern(Employee):
    def __init__(self):
        super().__init__()
    def work_hours(self):
        print("Interns works 6 hours a day")
s = Intern()
s.work_hours()
d = Employee()
d.work_hours()


class Customer:
    def __init__(self):
        pass
    def delivery_charge(self):
        print("delivery charge 50")
class PrimeCustomer(Customer):
    def __init__(self):
        super().__init__()
    def delivery_charge(self):
        print("delivery charge 20")
d=PrimeCustomer()
d.delivery_charge()
s=Customer()
s.delivery_charge()


class Ticket:
    def __init__(self):
        pass
    def price(self):
        print("TICKET price : $150")
class VipTicket(Ticket):    
    def __init__(self):
        super().__init__()
    def price(self):
        print("TICKET price :$500")
t1=Ticket()
t1.price()

    
class bank:
    def __init__(self):
        pass
    def interest_rate(self):
        print("interest rate : 4%")
class PrivateBank(bank):
    def __init__(self):
        super().__init__()
    def interest_rate(self):
        print("interest rate : 6%")
b1=PrivateBank()
b1.interest_rate()


class Course:
    def __init__(self):
        pass
    def course_fee(self):
        print("course fee: $5000")
class AdvancedCourse(Course):
    def __init__(self):
        super().__init__()
    def course_fee(self):
        print("course fee : $12000")
a1= AdvancedCourse()
a1.course_fee()
a2=Course()
a2.course_fee()

class Ride:
    def __init__(self):
        pass
    def fare(self):
        print("Fare: $100")
class LuxuryRide(Ride):
    def __init__(self):
        super().__init__()
    def fare(self):
        print("Fare: $300")
f1=LuxuryRide()
f1.fare()
f2=Ride()
f2.fare()


class Employee:
    def __init__(self):
        pass
    def bonus(self):
        print("Bonus: $5000")
class Manager(Employee):
    def __init__(self):
        super().__init__()
    def bonus(self):
        print("Bonus: $20000")
b1=Employee()
b1.bonus()
b2=Manager()
b2.bonus()

class Vehicle:
    def __init__(self):
        pass
    def max_speed(self):
        print("Maximum speed: 80 km/h")
class SportsCar(Vehicle):
    def __init__(self):
        super().__init__()
    def max_speed(self):
        print("Maximum speed: 250 km/h")
choice=input("enter your choice: ").strip()
if choice =="SportsCar":
    s=SportsCar()
    s.max_speed()
else:
    c=Vehicle()
    c.max_speed()

class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60 : ")
class AdvancedStudent:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80 : ")
p=input()
if p.lower() == "advancedstudent":
    p= Student()
else:
    p=AdvancedStudent()
p.placement_status()'''



#project
class Employee:
    def __init__(self,emply_id,emply_name):
        self.emply_id=emply_id
        self.emply_name=emply_name
class Fooditem:
    def __init__(self,item_name,price):
        self.item_name=item_name
        self.price=price
class Order:
    order_counter=1
    def __init__(self,Employee):
        self.order_id = Order.order_counter
        Order.order_counter +=1
        self.Employee=Employee
        self.ordered_items=[]
    def add_item(self,food_item):
        self.ordered_items.append(food_item)
    def calculate_total(self):
        return sum(item.price for item in self.ordered_items)
    def generate_bill(self):
        print("=" * 50)
        print(f"{'CORPORATE CAFETERIA BILL':^50}")
        print("=" * 50)
        print()
        print(f"Employee ID : {self.emply_id}")
        print(f"Employee Name : {self.emply_name}")
        print()
        print("-" * 50)
        print(f"{'Item':<30} {'Price':>15}")
        print("-" * 50)
        for item in self.ordered_items:
            print(f"{item.item_name:<30} ₹{item.price:>13}")
        print("-" * 50)
        print(f"{'Total Amount':<30} ₹{self.calculate_total():>13}")
        print()
        print(f"{'Payment Status':<30} {'PAID':>15}")
        print("=" * 50)


    

