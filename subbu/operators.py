x=12
y=4
print(f"addition of x & y is {x+y} ")
print(f"subtraction of x & y is {x-y}")
print(f"division of x & y is {x/y}")
print(f"multiplication of x & y is {x*y}")
print(f"modulo division of x & y is {x%y}")
print(f"positive floor divison of x & y is {x//y}")
print(f"negative floor divsion of x & y is {-x//y}")
print(f"exponential of x & y is {x**y}")


print(23<20)
print(23>20)
print(23<=23)
print(23>=20)
print(23==23)
print(23!=20)

a=10
print(f"a = {a}")
a+=2
print(f"a = {a}")
a-=3
print(f"a = {a}")
a*=5
print(f"a = {a}")
a/=6
print(f"a = {a}")


langa=15
print(langa>10 and langa<20)
print(langa>10 or langa<10)
print(not(langa<10))

langa=15
panga=10
print(langa & panga)
print(langa | panga)
print(langa << panga)
print(langa ^ panga)
print(~panga)
print(langa >> panga)


#in & not in
tuple=(10,30,40,50)
print(10 in tuple)
print(55 not in tuple)
print("Panja" in ' its a movie panja')
print("Panja" in ' its a movie Panja')

#is & is not
panja1= 45
print(panja1)
print(id(panja1))
panja2='subbu'
print(panja2)
print(id(panja2))
print(panja1 is not panja2)
print(panja2 is panja1)

#type coversions
tim1= ['cat','dog']
print(tim1)
print(type(tim1))
tim1=str(tim1)
print(type(tim1))

name= input("what is your name? ")
age=int(input("what is your age? "))
print("Hello," , name , "! You are", age ,"years old,")
print(f"Hello, {name}! You are {age} years old .")