print("Chason Qi")
print('*' * 10)
price = 10
rating = 4.9
name = "Chason"
is_published = True
print(price)

name = input("What is your name! ")
print("Hi " + name)

int()
float()
bool()

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

course = '''
this is a course
please mail to me
bye
'''
print(course)
print(name[0])
print(name[-1])
print(name[0:3])
print(name[0:])
print(name[:3])
print(name[1:-1])

first = 'John'
last = 'Smith'
message = first + ' [' + last +'] is a coder'
print(message)
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python is great'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find('P'))
print(course.find('Python'))
print(course.replace('Python', 'Java'))

print('is' in course)
print(course.title())

print(10/3)
print(10//3)
print(10 ** 3)
print(round(2.9))

print(abs(-2.9))
### print input int type float bool str
### f(格式化) len(长度) upper(大写) lower(小写) find(查找字符下标) replace(字符替换) in(是否在,返回布尔值), title(标题，将单词首字母大写)
### 单引号 双引号 三引号（多行）字符串索引，负指针
### python中字符串是不可变的
### //双斜线表示对结果取整 ** 冪指数 round(4舍5入)