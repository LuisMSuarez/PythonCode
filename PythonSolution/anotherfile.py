import sys
print(sys.argv[0])
print("Hello, World2!")
x = int(input("enter your number:"))
print("you entered", x)
myarray=[0,1,2]
print(len(myarray))
something = {}
something["pepe"]=1
something["nina"]=2
print(something["pepe"])
name1, age1 = something.items()
for name, age in something.items():
    print(name,age)
range(10)
