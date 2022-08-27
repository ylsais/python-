#集合类型
#集合类型有三个特点：无序；不重复；使用花括号表示

#集合示例
numbers={11,33,22,55,44,11,33}
print(numbers)
#运行结果 {33, 11, 44, 22, 55}

#1.remove(e)
numbers={11,33,22,55,44}
numbers.remove(22)          #使用remove(22)删除number中指定的元素22
print(numbers)
#运行结果  {33, 11, 44, 55}

#2.pop()
numbers={11,22,55,33,44}
numbers.pop()               #使用pop()删除numbers中的最后一个元素
print(numbers)
#运行结果 {11, 44, 22, 55}

#3.len()
numbers={11,33,22,55,44}
print(len(numbers))         #使用len(numbers)获得numbers的元素个素
#运行结果 5

#4.clear()
numbers={11,33,22,55,44}
numbers.clear()             #使用clear()清楚numbers的所有元素
print(numbers)
#运行结果 set()              #set()代表空集合

#5.add(e)
numbers={11,33,22,55,44}
numbers.add(66)             #使用add(66)向numbers中添加元素66
print(numbers)
#运行结果 {33, 66, 11, 44, 22, 55}

#6.union(e)
numbers={11,33,22,55,44}
num={66,77,88,99}
print(numbers.union(num))   #使用union(num)向numbers中添加指定集合num
#运行结果 {33, 66, 99, 22, 55, 88, 11, 44, 77}

