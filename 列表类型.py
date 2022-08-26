#列表类型
#1修改
list=['list','is',123,'a','number']  #声明列表并赋值
list[2]=567
print(list)

#2.append(e)
list=['list','is',123,'a','number']
list.append('here')         #使用append('here')向列表list的最后一位添加指定元素
print(list)

#3.inser(index,e)
list=['list','is',123,'a','number']
list.insert(0,'now')        #使用insert(0,'now')向列表list的第一位添加指定元素
print(list)

#4.remove(e)
list=['list','is',123,'a','number']
list.remove('is')           #使用remove('is')删除列表list中的制定元素
print(list)

#5.reverse()
names=['james','lucy','simon','tom']
names.reverse()             #使用reverse()将names中的元素顺序反向
print(names)

#6.sort()
names=[1,2,4,3]
names.sort()                #使用sort()将names中的元素进行排序
print(names)

#7.index(e)
list=['list','is',123,'a','number']
print(list.index('a'))      #使用index('a')匹配元素为‘a'的索引

#8.count(e)
list=['list','is',123,'a','number']
print(list.count('list'))   #使用count('list')统计元素为'list'的个数

#9.pop()
list=['list','is',123,'a','number']
list.pop()                 #使用pop()删除列表中的最后一个元素，返回元素的值
print(list)