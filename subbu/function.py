'''def greet():
    print("hello, guys")
greet()
greet()  

def add(a,b):
    print(f"addition of {a} and {b} is {a+b}")
add(7, 8)
add(10,14)

def add(a, b):
    return a+b
print(add(23, 67))
print(add(45, 78))

#program calculator
def add(a,b):
    print(f"addition of {a} and {b} is {a+b}")
def sub(a,b):
    print(f"subtraction of {a} and {b} is {a -b}")
def mul(a,b):
    print(f"multiplication of {a} and {b} is {a*b}")
def div(a,b):
    print(f"division of {a} and {b} is {a/b}")
def rem(a,b):
    print(f"remainder of {a} and {b} is {a%b}")
while True:
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. remainder")
    print("6. exit")
    choice=int(input("enter your choice: "))
    if choice == 6:
      break
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    if choice == 1:
      add(a,b)
    elif choice == 2:
      sub(a,b)
    elif choice == 3:
     mul(a,b)
    elif choice == 4:
     div(a,b)
    elif choice == 5:
     rem(a,b)
print("/n")

def one():
    def two():
       print("two")
    print("one")
one()

def openfoodapp():
    print("swiggy")
    searchfood()
    orderfood()
    deliveredfood()

def searchfood():
    print("search for food")
def orderfood():
    print("ordered food")
def deliveredfood():
    print("delivered food")

openfoodapp()

def read(bk):
    print("bk "+bk())
def do():
    return "dk"
read(do(read))

def total(*num):
    print(sum(num))
total(3,4,5)

square= lambda t:t*t
print(square(7))


area = lambda r: 3.14*r*r
print(area(5))


peoples=['uday','manideep','hemannth']
print("accessing the list using positive indexing")
print(peoples[0])
print(peoples[1])
print(peoples[2])

print("accessing the list using negative indexing")
print(peoples[-1])
print(peoples[-2])
print(peoples[-3])


peoples=['uday','manideep','hemannth']
for i in range(len(peoples)):
    print(f"index{i}: {peoples[i]}")

for i in peoples:
    print(i)

peoples=['uday','manideep','hemannth']
del peoples[1]
print(peoples)

chinthakayalu=[3,5,6,7,8,9,12]
print(chinthakayalu)
print(len(chinthakayalu))
print(max(chinthakayalu))
print(min(chinthakayalu))
print(sum(chinthakayalu))
print(sum(chinthakayalu)/len(chinthakayalu))
print(sorted(chinthakayalu))


sun=[20,30,40,50]
print(sun[:])
print(sun[0:3])
print(sun[::2])
print(sun[3:])
print(sun[-1:-3])
print(sun[::-1])

sun=[4,6,8,9,10,15]
moon=[2,4,5,8]
result= sun+moon
print(result)
result=sun*2
print(result)


size=int(input("enter the size of list: "))
Age=[]
for i in range(size):
    ele=int(input("enter the age: "))
    Age.append(ele)
print(Age)
for i in Age:
    if(i>=1 and i<=100):
        if(i<12):
            print(f"{i}-----> $10")
        elif(i>=12 and i<=60):
            print(f"{i}-----> $15")
        else:
            print(f"{i}------> $12")


pin=int(input("enter the pin: "))
acc_bal=0
if pin==2236:
    print("welcome to the bank ")
    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Blance inquiry")
        print("4. Exit")
        
        choice=int(input("enter your choice: "))
        print("/n")
        if choice==1:
            amount=int(input("enter the amount to deposit: "))
            acc_bal=acc_bal+amount
            print(f"dear customer your account xxxxxxxx5678 is credited with {amount}")
        elif choice==2:
            amount=int(input("enter the amount to withdrawal: "))
            if amount<acc_bal:
                print(f"dear customer your account xxxxxxx5678 is debited with {amount}")
                acc_bal=acc_bal-amount
            else:
                print("Insufficient balance...")
        elif choice==3:
            print(f"dear customer your account xxxxxxxx5678 has {acc_bal} .")
        else:
            print("thankyou...")
            break
else:
    print("you entered wrong pin.")

total=0
choice=int(input("enter your choice: "))
if choice== 1:
    print("1. small")
if choice== 2:
    print("2. medium ")
if choice== 3:
    print("3.large")
pizzanumber=int(input("enter no of pizzas: "))
for i in range(pizzanumber):
    choice=int(input("enter your choice: "))
    if choice== 1:
     print("1. small and cost--> $10")
     pizzacost=10
    if choice== 2:
     print("2. medium and costs--> $15")
     pizzacost=15
    if choice== 3:
     print("3. large and costs--> $20")
     pizzacost=20
toppings=int(input("enter the number of toppings: "))
toppings_cost=0
for i in range(toppings):
    print("1.cheese")
    print("2.pepperoni")
    print("3.olives")
    print("4.jalapenos")
    print("5.no toppings")
    choice=int(input("enter your choice: "))
    print("/n")
    if choice==1:
        print(f"added cheese and costs----> $2")
        toppingscost=2
        total=toppingscost
    elif choice==2:
        print(f"added  pepperoni and costs----> $3")
        toppingscost=3
        total=toppingscost
    elif choice==3:
        print(f"added olives and costs-----> $5")
        toppingscost=5
        total=toppingscost
    elif choice==4:
        print(f"added jalapenos and costs----> $5")
        toppingscost=5
        total=toppingscost
    elif choice==5:
        print("no toppings ")
    toppings_cost=toppingscost+toppings_cost

total=pizzacost+toppings_cost
print("total:",total)


list=[i for i in range(2,10,2)]
set={i for i in range(2,10,2)}
print(list)
print(sorted(set))

import copy 
subbu=[1,2,3,4,5]
print(subbu)
new=subbu
print(new)
new[0]=100
print(subbu)
print(new)

import copy 
subbu=[1,2,3,4,5]
print(subbu)
new=copy.deepcopy(subbu)
print(new)
new[0]=100
print(subbu)
print(new)


gammu=(1,2,3)
print(gammu)
a,b,f=gammu
print(a)
print(b)
print(f)'''

a =[1,2,35,6,8,6,5,8,99,0,66]
a.append(5)
print(a)
a.insert(2,85)
print(a)
a.remove(2)
print(a)

a.pop(0)
print(a)

a.index(85)
print(a.index(85))

a.count(2)
print(a.count(2))

a.sort()
print(a)

a.reverse()
print(a)

sum(a)
print(sum(a))

a.append(323)
print(a)

a.append(max(a))
print(a)

print(len(a))