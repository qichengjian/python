number = [0,1,2,3]
number.append(5)
print(number)

number.insert(0,199)
print(number)

number.remove(199)
print(number)

number.clear()
print(number)

number.pop()

number.index(2)
number.count(2)
number.sort()
number.reverse()
number2 = number.copy()
### append(追加元素) insert(按照索引位置添加元素) remove(移除指定元素) clear(清空)
### pop(移除队列末尾元素) index(元素对应的索引下标) count(相同元素的个数) sort(对队列进行排序) reverse(倒序)
### copy(复制队列)