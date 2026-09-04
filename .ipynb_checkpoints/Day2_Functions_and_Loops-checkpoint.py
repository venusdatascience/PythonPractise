password = "123xY@"

y = input("Enter password: ")
i =1
while i<=3:
    if y == password:
        print("Verify")
        break
    else:
        print("Try again")
        x = input("Enter combination of number, character and symbol: ")
        i+=1

print("your attem has expired")


        #• Fibonacci sequence 
def fibonacci(x):
    a = 0
    b = 1

    for i in range(x):
        print(a)

        c = a + b
        a = b
        b = c


y = int(input("Enter the number of terms: "))
fibonacci(y)

#factorial number
n =int(input("enter a number")) 
i = 1
result = n

while i < n:
    y = n - i
    result = result * y
    i += 1

print(result)

#prime number
def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            print("not a prime number")
            return

    print("prime number")

y = int(input("enter a number"))
prime_number(y)

#multiplication table generator

def mul_table(x):
  i =1
  while i<=10:
        y=x*i
        print(y)
        i+=1


mul_table(3)

#number gusing
number = 2

def new_number(x):
    while True:
        if x == number:
            return "your guess is correct"
        else:
            x = int(input("try again, enter a number: "))

y = int(input("enter a number: "))
print(new_number(y))
#student result

def student_result(name,marks):
    if marks>40:
        
        return "pass" ,name
    else:
        return "fail", name
    

x,y =student_result("nitu",65)
print(x,y)

#check value

def age(x):
    if x>18:
        return "adult"
        
    else:
        return "child" return can give value in condition staement  also

age(25)

#vCreate a function calculate_total(price, quantity) that calculates:

def calculate_total(price,quantity):
    total = price*quantity
    return total

calculate_total(3000,2)

#Create a function multiply(a, b) that prints the multiplication of two numbers.

def Multiplicationofnumber(x,y):
    return x*y#return can calculte values and return output
    
z = Multiplicationofnumber(2,3)
print(f"multiplication of two number is: {z}")

#Count positive and negative numbers
numbers = [10, -5, 7, -3, 8, -2, 4]
count = 0
count1 =0
for i in numbers:
    if i>1:
        count = count+1
    elif i<1:
        count1 = count1+1
        
print(f"the count o positive numbers {count}")
print(f"the count of negative numbers {count1}")
        