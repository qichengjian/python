try:
    age = int(input("Age: "))
    income = 10000;
    print(income/age)
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")

