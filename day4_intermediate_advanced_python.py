#expense tracker
expenses = {}


def add_expense():
    try:
        item = input("Enter item: ")
        cost = float(input("Enter cost: "))

        expenses[item] = cost

    except ValueError:
        print("Please enter a valid number.")


def show_expenses():
    print("\nYour Expenses:")

    for item, cost in expenses.items():

        if cost >= 1000:
            level = "High"
        elif cost >= 500:
            level = "Medium"
        else:
            level = "Low"

        print(item, ":", cost, "-", level)


# Add multiple expenses
while True:
    add_expense()

    again = input("Add another? yes/no: ")

    if again == "no":
        break


# Show expenses
show_expenses()


# Calculate total
total = 0

for cost in expenses.values():
    total = total + cost

print("\nTotal expense:", total)

#exception safe calcultor
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    def sum(x, y):
        return x + y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    print("Sum:", sum(x, y))
    print("Multiplication:", mul(x, y))
    print("Division:", div(x, y))

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

    #even number generator

def even_number(lis1):
    for i  in lis1:
        if i%2==0:
            yield i

lis1=[12,14,4,6,8]
print(list(even_number(lis1)))

for num in even_number(lis1):
    print(num)

    