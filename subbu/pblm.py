'''age=int(input("enter your age: "))
if(age>=18):
    print("are eligible to vote.")
else:
    print(" are not eligible to vote.")

#terinary operator
res="eligible" if age>=18 else "not eligible"
print("you are",res,"to vote.")


#2
uday=int(input("enter a number: "))
if(uday>0):
    print(f"{uday} uday is gay")
elif(uday<0):
    print(f"{uday} uday is not gay" )
else: 
    print(f"{uday} uday is nothing")

 #3
uday1=int(input("enter first uday"))
uday2=int(input("enter second uday" ))
if(uday1>uday2):
    print(f"{uday1} uday1 is big gay")
else:
    print(f"{uday1} uday2 is small gay3")

#4 
month=int(input("enter month number: "))
if(month>=1 and month<=12):
    print(month,"is valid.")
else:
    print(month,"is not valid.")

#5
marks=int(input("enter the marks:"))
if marks>=35 :
    print(f"{marks} is pass")
else:
    print(f"{marks} is fail")

#6 
for i in range(1,6):
    print("uday is not straight")

#7
uday=int(input("enter the code number:"))
for i in range(1,uday+1):
    print(i)

#8 
hemanth=int(input("enter the number: "))
for i in range(hemanth,0,-1):
    print(i)

#9
manideep=int(input("enter number:"))
for i in range(1,manideep+1):
    if i%2==0:
        print(i)
#10
sun=int(input("enter the number:"))
for i in range(1,sun+1):
    if i%2!=0:
        print(i)
#11
num=int(input("enter the numbber:"))
sum=0
for i in range(1,num+1):
   sum=sum+i
   print("the sum of first",num,"numbers is:",sum)

#12
num=int(input("enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)

#13
num=int(input("enter the numbers: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#14
num=int(input("enter the numbers: "))
for i in range(10,0,-16):
    print(f"{num} x {i} = {num*i}") 

#15
num=int(input("enter the number: "))
for i in range(1,num+1):
    print(f"multiplicaton table of {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

#16
num=int(input("enter the number: "))
for i in range(num,0,-1):
    print(f"multiplicaton table of {i}:")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}") 
#17
num=int(input("enter the number: "))
for i in range(1,num+1):
    print(f"multiplicaton table of {i}:")
    for j in range(10,0,-1):
        print(f"{i} x {j} = {i*j}")
#18
num=int(input("enter the number: "))
i=1
while i<=num:
    print(i)
    i+=1

#19
for i in range(1,11):
    if(i==5):
        break
    print(i)

num=int(input("enter the number"))
for i in range(1,11):
    if(i%2!=0):
         continue
    print(f"{num} x {i} = {num*i}") 

#20
num=int(input("enter the number:"))
count=0
rem=0
while(num!=0):
    rem=rem%10
    count+=1
    num=num//10
    print(f"count of digitd is {count}")'''

#21
num=int(input("enter the number:"))
sum=0
rem=0
while(num!=0):
    rem=num%10
    print(rem)
    num=num//10




