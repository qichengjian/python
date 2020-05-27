numbers = (1,2,3)
print(numbers[0])

coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z = coordinates

list = [1,2,3]
x,y,z = list

customer = {
    "name":"Smith",
    "age":20
}
print(customer["name"])
print(customer.get("birthday"))
print(customer.get("birthday", "defaultBirthday"))
###tuple元组 不可变结构
#### 字典（key-value形式，类似map）,直接方括号访问如果不存在就报错，用get访问不存在不报错 split


