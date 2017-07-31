#!/Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python
print ("Hello, Python!");

# if True:
#     print ("true");
#     print ("hello");
# else:
#     print ("false");

# input("\n\nPress the enter key to exit.");

# a = b = c = 1;
# print (a);
# print (b);
# print (c);
#
# a , b , c = 1 , 4 , "jlkasd";
# print (a);
# print (b);
# print (c);

print ("----------------");

# vara = 1;
# varb = 2;
# varc = varb;
# print (vara);
# print (varb);
# print (varc);

print ("-------Number---------");
# del varc;
# print (vara);
# print (varb);
# print (varc);


print ("-------字符串---------");
# str = "Hello World!"
# print (str);  # 输出完整字符串
# print (str[0]);  # 输出字符串中的第一个字符
# print (str[2:5]);  # 输出字符串中第三个至第五个之间的字符串
# print (str[2:]);  # 输出从第三个字符开始的字符串
# print (str * 2);  # 输出字符串两次
# print (str + "TEST");  # 输出连接的字符串


print ("-------列表---------");
# List = ["abcd", 786, 2.23, "john", 70.2]
# tinylist = [123, "john"]
#
# print (List);  # 输出完整列表
# print (List[0]);  # 输出列表的第一个元素
# print (List[1:3]);  # 输出第二个至第三个的元素
# print (List[2:]);  # 输出从第三个开始至列表末尾的所有元素
# print (tinylist * 2);  # 输出列表两次
# print (List + tinylist);  # 打印组合的列表


print ("-------元组---------");
# Tuple = ("abcd", 786, 2.23, "john", 70.2)
# tinytuple = (123, "john")
#
# print (Tuple);  # 输出完整元组
# print (Tuple[0]);  # 输出列表的第一个元素
# print (Tuple[1:3]);  # 输出第二个至第三个的元素
# print (Tuple[2:]);  # 输出从第三个开始至列表末尾的所有元素
# print (tinytuple * 2);  # 输出元组两次
# print (Tuple + tinytuple);  # 打印组合的元组
#
# print ("-------元组不允许更新 , 但是列表允许---------");
# Tuple = ( "abcd", 786 , 2.23, "john", 70.2 )
# List = [ "abcd", 786 , 2.23, "john", 70.2 ]
# # Tuple[2] = 1000 # 错误！元组中是非法应用
# List[2] = 1000 # 正确！列表中是合法应用


print ("-------字典---------");
# dict = {}
# dict["one"] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {"name": "john", "code": 6734, "dept": "sales"}
#
# print (dict["one"]);  # 输出键为"one" 的值
# print (dict[2]);  # 输出键为 2 的值
# print (tinydict);  # 输出完整的字典
# print (tinydict.keys());  # 输出所有键
# print (tinydict.values());  # 输出所有值
#
# aaa = eval("print ('kkkk')");
# print (aaa);


print("-------Python数据类型转换--------");
# 数据类型的转换，你只需要将数据类型作为函数名即可
# 函数	描述
# int(x [,base])
# 将x转换为一个整数
# long(x [,base] )
# 将x转换为一个长整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# unichr(x)
# 将一个整数转换为Unicode字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串


print("-------运算符---------");
# 算术运算符
# + , - , * , / , % , ** , //
# **: x ** y  -->  返回x的y次幂
# //: x // y  -->  返回商的证书部分

# 比较运算符
# == , != , <> , > , < , >= , <=
# !=(3.0版本之后) 和 <>(2.6版本之前) 都是比较两个对象是否不相等

# 赋值运算符
# = , += , -= , *= , /= , %= , **= , //=

# 位运算符
# & , | , ^ , ~ , << , >>

# 逻辑运算符
# and , or , not

# 成员运算符(包括字符串，列表或元组)
# in , not in

# 身份运算符(身份运算符用于比较两个对象的存储单元)
# is , is not
# x is y , 如果 id(x) 等于 id(y) , is 返回结果 1

# python中运算符的优先级问题
# 运算符	描述
# **	指数 (最高优先级)
# ~ + -	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % //	乘，除，取模和取整除
# + -	加法减法
# >> <<	右移，左移运算符
# &	位 'AND'
# ^ |	位运算符
# <= < > >=	比较运算符
# <> == !=	等于运算符
# = %= /= //= -= += *= **=	赋值运算符
# is is not	身份运算符
# in not in	成员运算符
# not or and	逻辑运算符


print("-------条件语句-------");
# if 判断条件：
#     执行语句……
# else：
#     执行语句……


print("-------循环语句-------");
# 循环语句中会出现控制语句 break , continue , pass
# 其中pass是空语句 , 是为了保持程序结构的完整性

# while 循环
# count = 0
# while (count < 9):
#    print 'The count is:', count
#    count = count + 1

# for循环
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print 'Current fruit :', fruit
# 带index的for循环
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print 'Current fruit :', fruits[index]
# for....else   -------> for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
# for num in range(10,20):  #to iterate between 10 to 20
#    for i in range(2,num): #to iterate on the factors of the number
#       if num%i == 0:      #to determine the first factor
#          j=num/i          #to calculate the second factor
#          print '%d equals %d * %d' % (num,i,j)
#          break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print num, 'is a prime number'



print ("-------Python中的数学函数-------");
# 函数	返回值 ( 描述 )
# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j


print ("-------Python中的随机数函数-------");
# 函数	描述
# choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# random()	随机生成下一个实数，它在[0,1)范围内。
# seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	将序列的所有元素随机排序
# uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。


print ("-------Python中的三角函数-------");
# 函数	描述
# acos(x)	返回x的反余弦弧度值。
# asin(x)	返回x的反正弦弧度值。
# atan(x)	返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	返回的x弧度的正弦值。
# tan(x)	返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如math.degrees(math.tan(1.0)) ,返回30.0
# radians(x)	将角度转换为弧度


print ("-------Python中的数学常量-------");
# 常量	描述
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	数学常量 e，e即自然常数（自然常数


print("-----------格式化字符串----------");
print ("My name is %s and weight is %d kg!" % ('Zara', 21));
# 格式化操作符辅助指令:
# 符号	功能
# *	定义宽度或者小数点精度
# -	用做左对齐
# +	在正数前面显示加号( + )
# <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格
# %	'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

# 三引号 可以将字符串原样输出
# 一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

# Unicode 字符串
# u'Hello\u0020World !'
# u'Hello World !'

# 字符串方法
# 方法	描述
# string.capitalize()
# 把字符串的第一个字符大写
# string.center(width)
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# string.count(str, beg=0, end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
# string.decode(encoding='UTF-8', errors='strict')
# 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
# string.encode(encoding='UTF-8', errors='strict')
# 以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
# string.endswith(obj, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
# string.expandtabs(tabsize=8)
# 把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
# string.find(str, beg=0, end=len(string))
# 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# string.index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在 string中会报一个异常.
# string.isalnum()
# 如果 string 至少有一个字符并且所有字符都是字母或数字则返
# 回 True,否则返回 False
# string.isalpha()
# 如果 string 至少有一个字符并且所有字符都是字母则返回 True,
# 否则返回 False
# string.isdecimal()
# 如果 string 只包含十进制数字则返回 True 否则返回 False.
# string.isdigit()
# 如果 string 只包含数字则返回 True 否则返回 False.
# string.islower()
# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# string.isnumeric()
# 如果 string 中只包含数字字符，则返回 True，否则返回 False
# string.isspace()
# 如果 string 中只包含空格，则返回 True，否则返回 False.
# string.istitle()
# 如果 string 是标题化的(见 title())则返回 True，否则返回 False
# string.isupper()
# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# string.join(seq)
# Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# string.ljust(width)
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# string.lower()
# 转换 string 中所有大写字符为小写.
# string.lstrip()
# 截掉 string 左边的空格
# string.maketrans(intab, outtab])
# maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# max(str)
# 返回字符串 str 中最大的字母。
# min(str)
# 返回字符串 str 中最小的字母。
# string.partition(str)
# 有 点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
# string.replace(str1, str2,  num=string.count(str1))
# 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
# string.rfind(str, beg=0,end=len(string) )
# 类似于 find()函数，不过是从右边开始查找.
# string.rindex( str, beg=0,end=len(string))
# 类似于 index()，不过是从右边开始.
# string.rjust(width)
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# string.rpartition(str)
# 类似于 partition()函数,不过是从右边开始查找.
# string.rstrip()
# 删除 string 字符串末尾的空格.
# string.split(str="", num=string.count(str))
# 以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
# string.splitlines(num=string.count('\n'))
# 按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
# string.startswith(obj, beg=0,end=len(string))
# 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
# string.strip([obj])
# 在 string 上执行 lstrip()和 rstrip()
# string.swapcase()
# 翻转 string 中的大小写
# string.title()
# 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
# string.translate(str, del="")
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符,
# 要过滤掉的字符放到 del 参数中
# string.upper()
# 转换 string 中的小写字母为大写
# string.zfill(width)
# 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
# string.isdecimal()
# isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。


print("----------列表方法---------");
# del list1[2];
# 删除列表元素

# Python列表脚本操作符
# Python 表达式	结果	描述
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3	迭代

# Python列表截取
# L = ['spam', 'Spam', 'SPAM!']
# Python 表达式	结果	描述
# L[2]	'SPAM!'	读取列表中第三个元素
# L[-2]	'Spam'	读取列表中倒数第二个元素
# L[1:]	['Spam', 'SPAM!']	从第二个元素开始截取列表

# Python列表函数&方法
# cmp(list1, list2)
# 比较两个列表的元素
# len(list)
# 列表元素个数
# 	max(list)
# 返回列表元素最大值
# 	min(list)
# 返回列表元素最小值
# 	list(seq)
# 将元组转换为列表
# 	list.append(obj)
# 在列表末尾添加新的对象
# list.count(obj)
# 统计某个元素在列表中出现的次数
# list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)
# 将对象插入列表
# list.pop([index])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 	list.reverse()
# 反向列表中元素
# list.sort([func])
# 对原列表进行排序

print("---------元组--------");
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 如下实例：
# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5 );
# tup3 = "a", "b", "c", "d";

# 创建空元组
# tup1 = ();
# 元组中只包含一个元素时，需要在元素后面添加逗号
# tup1 = (50,);

# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
# tup1 = (12, 34.56);
# tup2 = ('abc', 'xyz');
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100;
# # 创建一个新的元组
# tup3 = tup1 + tup2;
# print tup3;
# 以上实例输出结果：
# (12, 34.56, 'abc', 'xyz')

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
# tup = ('physics', 'chemistry', 1997, 2000);
# print tup;
# del tup;
# print "After deleting tup : "
# print tup;
# 以上实例元组被删除后，输出变量会有异常信息

# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# Python 表达式	结果	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ['Hi!'] * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print x,	1 2 3	迭代

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
# 元组：
# L = ('spam', 'Spam', 'SPAM!')
# Python 表达式	结果	描述
# L[2]	'SPAM!'	读取第三个元素
# L[-2]	'Spam'	反向读取；读取倒数第二个元素
# L[1:]	['Spam', 'SPAM!']	截取元素

# 元组内置函数
# Python元组包含了以下内置函数
# 序号	方法及描述
# 1	cmp(tuple1, tuple2)
# 比较两个元组元素。
# 2	len(tuple)
# 计算元组元素个数。
# 3	max(tuple)
# 返回元组中元素最大值。
# 4	min(tuple)
# 返回元组中元素最小值。
# 5	tuple(seq)
# 将列表转换为元组。


print("---------字典---------");
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行

# 删除字典元素
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
# del dict['Name'];  # 删除键是'Name'的条目
# dict.clear();  # 清空词典所有条目
# del dict;  # 删除词典

# 字典内置函数&方法
# Python字典包含了以下内置函数：
# 序号	函数及描述
# 1	cmp(dict1, dict2)
# 比较两个字典元素。
# 2	len(dict)
# 计算字典元素个数，即键的总数。
# 3	str(dict)
# 输出字典可打印的字符串表示。
# 4	type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。
# Python字典包含了以下内置函数：
# 序号	函数及描述
# 1	radiansdict.clear()
# 删除字典内所有元素
# 2	radiansdict.copy()
# 返回一个字典的浅复制
# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
# 5	radiansdict.has_key(key)
# 如果键在字典dict里返回true，否则返回false
# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组
# 7	radiansdict.keys()
# 以列表返回一个字典所有的键
# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里
# 10	radiansdict.values()
# 以列表返回字典中的所有值


print("----------日期和时间----------");
# import time;
# ticks = time.time()
# print ("Number of ticks since 12:00am, January 1, 1970:", ticks);

# # 获取当前时间
# # 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
# localtime = time.localtime(time.time())
# print ("Local current time :", localtime);

# 获取格式化的时间
# 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
# localtime = time.asctime(time.localtime(time.time()))
# print ("Local current time :", localtime);

# 获取某月日历
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
# import calendar

# cal = calendar.month(2008, 1)
# print ("Here is the calendar:" , cal);

# Time模块
# Time模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：
# 序号	函数及描述
# 1	time.altzone
# 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# 2	time.asctime([tupletime])
# 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# 3	time.clock( )
# 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# 4	time.ctime([secs])
# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
# 5	time.gmtime([secs])
# 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# 6	time.localtime([secs])
# 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
# 7	time.mktime(tupletime)
# 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
# 8	time.sleep(secs)
# 推迟调用线程的运行，secs指秒数。
# 9	time.strftime(fmt[,tupletime])
# 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
# 根据fmt的格式把一个时间字符串解析为时间元组。
# 11	time.time( )
# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 12	time.tzset()
# 根据环境变量TZ重新初始化时间相关设置。
# Time模块包含了以下2个非常重要的属性：
# 序号	属性及描述
# 1	time.timezone
# 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
# 2	time.tzname
# 属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

# 日历（Calendar）模块
# 此模块的函数都是日历相关的，例如打印某月的字符月历。
# 星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
# 序号	函数及描述
# 1	calendar.calendar(year,w=2,l=1,c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# 2	calendar.firstweekday( )
# 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
# 3	calendar.isleap(year)
# 是闰年返回True，否则为false。
# 4	calendar.leapdays(y1,y2)
# 返回在Y1，Y2两年之间的闰年总数。
# 5	calendar.month(year,month,w=2,l=1)
# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
# 6	calendar.monthcalendar(year,month)
# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# 7	calendar.monthrange(year,month)
# 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
# 8	calendar.prcal(year,w=2,l=1,c=6)
# 相当于 print calendar.calendar(year,w,l,c).
# 9	calendar.prmonth(year,month,w=2,l=1)
# 相当于 print calendar.calendar（year，w，l，c）。
# 10	calendar.setfirstweekday(weekday)
# 设置每周的起始日期码。0（星期一）到6（星期日）。
# 11	calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
# 12	calendar.weekday(year,month,day)
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。


print("----------函数的定义与使用-------");
print("------请参考地址: http://www.okpython.com/view-21-1.html ------------");



print("------模块化加载-----");
# import aname;
# aname.print_fun("liuxiangyu");


print("------导入模块的某一个函数-----");
# from aname import functionB;
# functionB();

# content = dir(aname);
# print(content);
# print (aname.__file__);

# 返回的是所有能在该函数里访问的命名
# print(locals());
# 返回的是所有在该函数里能访问的全局名字
# print(globals());

# # 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
# # 因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块
# import importlib;
# importlib.reload(aname);

# import Phone
# Phone.Pots()
# Phone.Isdn()
# Phone.G3()


print("------文件读写-----");
# fo = open("fileTest.txt" , "w+");
# print(fo);
# print(fo.name);
# print(fo.mode);
# # print(fo.softspace );
# fo.write( "Python is a great language.\nYeah its great!!\n");
# fo.write( "Python is a great language.\nYeah its great!!\n");
# fo.close();

# fo = open("fileTest.txt" , "r+")
# str = fo.read( 20);
# print(str);

# fo = open("fileTest.txt" , "r+");
# str = fo.read(10);
# print(str);
# # 查看指针当前位置
# position = fo.tell();
# print(position);
# str = fo.read(10);
# print(str);

# # 重新定位指针位置
# # seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# # 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
# position = fo.seek(1 , 0);
# print (position);
# str = fo.read(10);
# print (str);



import os
# 引入os模块开始对文件进行文件处理操作方法
# os.rename("fileTest.txt" , "test.txt");

# os.remove("wo.txt");

# os.mkdir("test")

# os.mkdir("home")

# print(os.getcwd());

# os.chdir("test")
# os.mkdir("home1")

# print(os.getcwd());

# os.rmdir("test/home1")


# # 判断一个数据是否是可迭代对象
# from collections import Iterable
# print(isinstance("abc" , Iterable));

# for i , value in enumerate(["a" , "b" , "c"]):
#     print (i , value);

# a = [x for x in range(1 , 11)]
# print(a);

# a = [x for x in range(1 , 11) if x % 2 == 0]
# print(a);

# a = [m + n for m in "ABC" for n in "abc"]
# print(a);

# #列车当前目录下的所有文件和目录名
# import os
# a = [d for d in os.listdir(".")];
# print(a);

# b = {"name":"zhangsan" , "age":"12" , "hobby":"python"};
# a = [k + "=" + v for k , v in b.items()]
# print(a);

# 把一个list中所有的字符串变成小写
# b = ["Hello" , "Python"];
# a = [s.lower() for s in b]
# print(a);

# b = ["Hello" , 12 , "Python" , 15 , "web前段"];
# a = [s.lower() for s in b if isinstance(s , str)]
# print(a);

# a = [x for x in range(1 , 11)];
# print(a);
#
# b = (x for x in range(1 , 11));
# print(b);
# print(next(b));
# print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));
# print(next(b));print(next(b));

# for n in b:
#     print(n);


# 斐波那契数列 (兔子繁殖)  得到数据
# def fib(max):
#     n , a , b = 0 , 0 , 1;
#     while n < max:
#         print(b);
#         a , b = b , a+b;
#         n = n + 1;
#     return "done";
#
# fib(6);

# 优化
# def fib(max):
#     n , a , b = 0 , 0 , 1;
#     while n < max:
#         yield b;
#         a , b = b , a+b;
#         n = n + 1;
#     return "完成";
#
# f = fib(6);
# print(f);

# for n in f:
#     print(n);

# # 测试一下下面这个例子(再来理解到底是什么意思)
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
# 我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
# 怎样才能拿到return中的"完成"呢
# 必须捕获 StopIteration错误  才能让 yield() 走完
# while True:
#     try:
#         x = next(f);
#         print("f:" , x);
#     except StopIteration as e:
#         print("Generator 走return了 , 内容是: " , e.value);
#         break;


# from PIL import Image
#
# im = Image.open('4.jpg');
# print(im);

# im.thumbnail((100 , 200));
# im.save("5.jpg" , "JPEG");

# import os
# print(os.path);
#
# import sys
# print(sys.path);

# 判断一个对象是否是函数
# def fn():
#     pass

# import types
# print(type(fn) == types.FunctionType);
# print(type(abs) == types.BuiltinFunctionType);
# print(type(lambda x: x) == types.LambdaType);
# print(type((x for x in range(10))) == types.GeneratorType);

# # 获得一个对象的所有属性和方法
# print(dir("abc"));
# print("abddd".__len__());



print("-------进程和线程---------");
# import os;
# print("父进程的ID....." , os.getpid());
#
# pid = os.fork();
# if pid == 0:
#     print("我是子进程%s , 我的父进程是%s"%(os.getpid() , os.getppid()));
# else:
#     print("我是%s , 刚刚创建了一个子进程%s"%(os.getpid() , pid));

# 快平台 多进程模块  multipricessing
# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print("run 子进程(%s)(%s)" % (name , os.getpid()));
# if __name__ == "__main__":
#     print("父进程是:%s" % os.getpid());
#     p = Process(target=run_proc , args=("ziJinCheng" , ));
#     print ("子进程将要开始了.....");
#     p.start();
#     p.join();
#     print ("子进程结束.....");

# 通过进程池的方式 批量创建子进程
# from multiprocessing import Pool
# import os , time , random
# def long_time_task(name):
#     print("Run task %s (%s)...." % (name , os.getpid()));
#     start = time.time();
#     time.sleep(random.random() * 4);
#     end = time.time();
#     print("task %s runs %0.2f seconds.." % (name , (end - start)));
#
# if __name__ == "__main__":
#     print("Parent process is %s..." % os.getpid());
#     p = Pool(2);
#     for i in range(5):
#         p.apply_async(long_time_task , args=(i , ))
#     print ("等待所有的子进程执行完毕.....");
#     p.close();
#     p.join();
#     print("所有子进程done了...");


# 控制子进程的输入输出
# import subprocess
# print("$ nslookup www.python.org");
# r = subprocess.call(["nslookup" , "www.baidu.com"]);
# print ("Exit code: " , r);

# 通过 communicate() 方法来实现子线程的输入
# import subprocess
# print ("$ nslookup....");
# p = subprocess.Popen(["nslookup"] , stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE);
# output , err = p.communicate(b'set q=mx\npython.org\nexit\n');
# print(output.decode('utf-8'));
# print('Exit code: ' , p.returncode);


# 进程之间的通信
# from multiprocessing import Process , Queue
# import os , time , random
#
# # 写数据进程执行的代码
# def write(q):
#     print("Process to write: %s" % os.getpid());
#     for value in ["A" , "B" , "C"]:
#         print("put %s to queue...." % value);
#         q.put(value);
#         time.sleep(random.random());
#
# # 读数据进程执行的代码
# def read(q):
#     print("Process to read: %s" % os.getpid());
#     while True:
#         value = q.get(True);
#         print("Get %s from queue.." % value);
#
# if __name__ == "__main__":
#     # 父进程创建Queue , 并传递给各个子进程
#     q = Queue();
#     pw = Process(target=write , args=(q , ));
#     pr = Process(target=read , args=(q , ));
#
#     pw.start();
#
#     pr.start();
#
#     pw.join();
#
#     pr.terminate();


# 启动一个线程
# import time , threading
# def loop():
#     print("thread %s is running...." % threading.current_thread().name);
#     n = 0;
#     while n < 5:
#         n = n + 1;
#         print("thread %s >>>> %s" % (threading.current_thread().name , n));
#         time.sleep(1);
#
#     print("thread %s ended ..." % threading.current_thread().name);
#
# print ("thread %s is running .." % threading.current_thread().name);
# t = threading.Thread(target=loop , name="LoopThread");
# t.start();
# t.join();
# print ("thread %s ended" % threading.current_thread().name);


# 多线程同时操作一个变量
# import time , threading
#
# lock = threading.Lock();
# balance = 0;
# def change_it(n):
#     global balance;
#     balance = balance + n;
#     balance = balance - n;
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire();
#         try:
#             change_it(n);
#         finally:
#             lock.release();
#
# t1 = threading.Thread(target=run_thread , args=(5 , ));
# t2 = threading.Thread(target=run_thread , args=(8 , ));
#
# t1.start();
# t2.start();
# t1.join();
# t2.join();
#
# print (balance);

# 图片处理
# from PIL import Image , ImageFilter
# im = Image.open("4.jpg");
# im2 = im.filter(ImageFilter.BLUR);
# im2.save("blur.jpg" , "jpeg");
# print(ImageFilter);


# 生成验证码图片
# # https://pillow.readthedocs.io/en/4.2.x/
# from PIL import Image , ImageDraw , ImageFont , ImageFilter
# import random
#
# def rndChar():
#     return chr(random.randint(65 , 90));
# def rndColor():
#     return (random.randint(64 , 255) , random.randint(64 , 255) , random.randint(64 , 255));
# def rndColor2():
#     return (random.randint(32 , 127) , random.randint(32 , 127) , random.randint(32 , 127));
#
# width = 60 * 4;
# height = 60;
#
# image = Image.new("RGB" , (width , height) , (100 , 100 , 100));
# font = ImageFont.truetype("Arial.ttf" , 36);
# draw = ImageDraw.Draw(image);
#
# for x in range(width):
#     for y in range(height):
#         draw.point((x , y) , fill=rndColor());
#
# for t in range(4):
#     draw.text((60 * t + 10 , 10) , rndChar() , font=font , fill=rndColor2());
#
# image = image.filter(ImageFilter.BLUR);
# image.save("code.jpg" , "JPEG");

# Tkiinter
# import tkinter as tk
#
# root = tk.Tk()
# # top=Tkinter.Tk()#创建一个顶层窗口对象
#
# label = tk.Label(root, text='hell world')
# label.pack()
# button = tk.Button(root , text="button");
# button.pack();
# tk.mainloop()  # 进入主事件循环


# TCP连接
# import socket
# s = socket.socket(socket.AF_INET , socket.SOCK_STREAM);
# s.connect(("www.sina.com.cn" , 80));
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 开始接受数据
# buffer = [];
# while True:
#     d = s.recv(1024);
#     if d:
#         buffer.append(d);
#     else:
#         break;
# data = b''.join(buffer);
# s.close();
#
# header , html = data.split(b'\r\n\n' , 1);
# # print(header.decode("utf-8"));
#
# with open("sina.html" , "wb") as f:
#     f.write(html)



# 注意 变成generator的函数，在首次调用的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# def consumer():
#     r = ''
#     print('lalalalalaal') # 只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
#     while True:
#         n = yield r # 再次执行时从这里的yield继续执行, 将把produce传入的参数 n 赋给局部变量 n . 下轮循环再次遇到yield就会就将 r 返回给produce函数
#         # 所以Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
#         print('xxxxxlalalalalaal')  # 由于生成器在启动的时候遇到上面的yield就返回了, 所以第一次不会执行这条语句. 之后每次都会被执行
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'  # 因为yield r 所以这个r会在下一次循环被返回给produce函数
#         a = 'fake 200 OK' # 返回的值与a无关
#
# def produce(c):
#     c.send(None)
#     print('babababab')
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n) # # 获取生成器consumer中由yield语句返回的下一个值
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()      # 并不会启动生成器, 只是将c变为一个生成器
# print('AaAaAaAaAa') # AaAaAaAaAa
# produce(c)


# import webbrowser as web
# url = "http://www.tudou.com/programs/view/myLEA7IrHx4/";
# web.open_new_tab(url);


# 提取网络地址
import urllib.request
f = urllib.request.urlopen("http://www.tudou.com/home/item_u121551255s0p1.html");
sa = f.read();
# print(sa);

# 开始提取网址
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(sa , "html.parser")
#
# tag = soup.findAll("a");
# print(tag);
#
# i = 0;
# for hr in tag:
#     url = hr.get("href");
#     print(i , url);
#     i += 1;
