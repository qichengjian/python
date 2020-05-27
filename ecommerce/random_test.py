import random

print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ["John", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second  ###返回一个元组，可以省略元组的小括号


dice = Dice()
print(dice.roll())
### random内置对象 ，random随机0-1之间的小数，randint随机整数，choice随机获取列表中的值