#字典类型
#该函数接收一个集合作为参数，作用是合并两个集合

#字典示例
dictionary={'name':'simon','age':20}
print(dictionary)
#运行结果 {'name': 'simon', 'age': 20}
print(dictionary['name'])
#运行结果 simon

#1.len(d)
dictionary={'name':'simon','age':20}
print(len(dictionary))                  #使用len(dictionary)获得字典的元素个数
#运行结果 2

#2.clear()
dictionary={'name':'simon','age':20}
dictionary.clear()                      #使用clear()清除字典的所有元素
print(dictionary)
#运行结果 {}

#3.copy()
dictionary={'name':'simon','age':20}
dictionary_new=dictionary.copy()        #使用copy()复制字典dictionary的元素，并赋值给新的字典dictionay
print(dictionary_new)
#运行结果 {'name': 'simon', 'age': 20}

#4.get(key,default=None)
dictionary={'name':'simon','age':20}
value=dictionary.get('name')           #使用get('name')获得键为'name'的值
print(value)
#运行结果 simon
print(dictionary.get('gender'))        #使用get('gender')获得键为'gender'的值
#运行结果  None                         #由于键'gender'不存在，因此返回None

#5.keys()
dictionary={'name':'simon','age':20}
list=dictionary.keys()                  #使用keys()获得字典dictionary中的所有键
print(list)
#运行结果 dict_keys(['name', 'age'])     #以列表形式返回

#6.values
dictionary={'name':'simon','age':20}
list=dictionary.values()                #使用values()获得字典dictionary中的所有值
print(list)
#运行结果  dict_values(['simon', 20])    #以列表形式返回