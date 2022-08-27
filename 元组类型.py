#元组类型
#元组示例
tuple1=(12,34,56)        #定义一个元组
print(tuple1)
#运算结果 (12, 34, 56)
print(tuple1[1])         #使用数组下标获取元组的元素
#运算结果 34

#1.len(t)
tuple1=(1,2,3,4)
print(len(tuple1))      #使用len(tuple1)获得元组的元素个数
#运算结果 4

#2.max(t)
tuple1=(1,2,3,4)
print(max(tuple1))      #使用max(tuple1)获得元组中的最大值
#运算结果 4

#3.min(t)
tuple1=(1,2,3,4)
print(min(tuple1))      #使用min(tuple1)获得元组中的最小值
#运算结果 1

#4.tuple(liat)
list=['this','is',123,'a','number']
print(tuple(list))    #使用tuple(list)将列表转换为元组
#运算结果 ('this', 'is', 123, 'a', 'number')