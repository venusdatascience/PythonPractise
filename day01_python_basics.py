# 1 create varables describing information about person

name = "Rina"
_age=27
FavouriteColour = "Red"
bestPlace = "Ktm"
best_food="Pasta"
print(f"Information about {name} : she is {_age} years old.her favroutie colour is{FavouriteColour},she likes to visit {bestPlace} and she likes to eat {best_food}")

#swaping a number
x=3
y= 4
x,y=y,x
print(x)

print(y)

#example product information
product_name= "Laptop"
productPrice = 50000
ProductRating = 4.5
is_available = True

print("Product Name: {}, Price: {}, Rating: {}, Available: {}".format(
    product_name, productPrice, ProductRating, is_available))

#example student result system
StudentName = "Ram"

math = 87
science = 78
english = 89

subjects = ['math','science','english']
total_marks = math+science+english
percentage = (total_marks/3)*100
is_pass = math>=40 and science>=40 and english>=40


print(f"student name:{StudentName}")
print(f"TotalMarks:{total_marks}")
print(f"Percentage:{percentage}")
print(f"Passed: {is_pass}")

print('computer' in subjects)
print('math' in subjects)

#example 2 employee salary and permission system

employee_name = input("enter employee name")
salary = int(input("enter salary"))
salary+=4000

print(salary)
experience =float(input("enter year of experience"))
is_senior = experience>=4.6


is_active = True


can_get_bonus = salary>=5000 and is_active


permission =["read","write"]

can_write = ("write" in permission)




print("Employee:", employee_name)
print("Salary:", salary)
print("Senior:", is_senior)
print("Bonus Eligible:", can_get_bonus)
print("Can Write:", can_write)
                    

      #checking vowel
x = 'w'
y =['a','e','i','o','u']
is_vowel= x in y
print(f" is given letter  vowel:{is_vowel}")

  # Create a simple student-information prog

name = input("enter name ")
age = int(input("age"))
school = input("school")
subject = input("sunject")
marks = float(input("mark"))

print("........STUDENT INFORMATION........")
print (f"Name of student: {name} \n Age of Student: {age} \n School: {school})\n Subject:{subject} \n Marks:{marks}")

   # Reverse a string.

str = "machinelearning"

print(str[-1::-1])

#Count characters in a string.

program = "Datascience python and machine learning"



print("count of a character  ",program.count("a"))

count =len(program)
print(f"total numbers of charcters : {count}")

#Convert Celsius to Fahrenheit.

celsius = float(input("enter temperature in celsius"))

Fahrenheit = (celsius+9/5)+32



print(f"temperature in farenhite is {Fahrenheit}")

   #Check whether a number is even or odd.

number = int(input("enter a number"))

is_even = number%2==0
is_odd = number%2!=0

print(is_even)
print(is_odd)

#Create a calculator.

x = int(input("enter a number"))
y = int(input("enter another number"))
print("addition",x+y)
print("substraction",x-y)
print("multiplication",x*y)
print("division",x/y)
