print('hii');

def hii():
    print('hii from hii() function')

hii()

def myfnction():
    print("hii",hii())
myfnction()
name="sibghatullah"
age=20
price=1000.50 
print(name)
print(age)  
print(price)



a,b=2,1
txt="hello world \n"

print(a*txt*b)

name=input("Enter your name: ")



if(name == "sibghatullah"):
    print("Welcome back, hiie!")
elif(name == "john"):
    print("Hello, name! Nice to see you again.")
else:
    print("Hello, " + name + "! It's nice to meet you.")


light=input("light:")
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")  

elif(light=="yellow"):
    print("Get ready to stop")
else:
    print("Invalid light color")


#ternary operator example
print("stop") if light == "red" or light == "yellow" else print("Go") if light == "green" else print("Invalid light color")

 

# This is a simple Python script that demonstrates basic input/output, conditional statements, and a function definition.
# It includes a greeting based on user input and a traffic light simulation.