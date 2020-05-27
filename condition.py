is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Smith for loan")
if has_high_income or has_good_credit:
    print("bank for loan")
if has_high_income and not has_good_credit:
    print("egg for loan")


i = 1
while i <= 5:
    print('*' * i)
    i +=1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

for item in 'python':
    print(item)

for item in ['python', 'java', 'php']:
    print(item)

for item in range(4): ###0，1，2，3
    print(item)
for item in range(2,5): ###2,3,4
    print(item)
for item in range(2,5,2): ###2,4
    print(item)

matrix = [
    [0,1,2],
    [2,2,2],
    [3,2,1]
]
print('matrix: ' + str(matrix[0][1]))
### if elif else and or not while break continue for range(数字范围函数)