x=20
y=3.14
name="Sibghat"
is_active=True

total=x+y
power=x**y
is_equal=(x==y)

greeeting=name+"!"
repeated=name*2
print(total,power,is_equal,greeeting,repeated)






x=10
if x>0:
    print("positive")
elif x==0:
    print("zero")
else:
    print("Negative")
          
for i in range(5):
    print(i,end=" ")
    
count=0
while count<3:
    print("count is",count)
    count+=1

evens =[x for x in range(10) if x%2==0]
print("Even numbers:", evens)

for i in range(10):
    if(i ==5):
        break
    if(i%2==0):
        continue
    print(i)