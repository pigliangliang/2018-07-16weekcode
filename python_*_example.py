#author_by zhuxiaoliang
#2018-07-24 上午9:22
#*用于解包，比如打印列表
l = [1,2,5]
print(l)
print(*l)#将列表中的元素进行解包
d = {
    'a':1,
    'b':2,
}
print(*d)#解包字典得到key

'''
输出：
[1, 2, 5]
1 2 5
a b
'''
#*将列表中的元素解包为单个元素
'''

def accept(*s):
    print(sum(s))
list = (0, 1, 2, 3, 7.5)
print(sum(list))
accept(*list)'''
#对于k，v形式的参数需要使用**进行解包

def accept(**s):
    print(s)
list = {
    'a':1,
    'b':2,
    'c':3,
}

accept(**list)
'''
1、函数声明的参数列表中加*号表示传入的参数为一个列表或者元组，**则传入字典。
2、在变量前加*号表示将列表等容器拆分为单个元素，**号则为对字典拆分
'''
