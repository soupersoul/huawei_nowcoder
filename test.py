import re
s='人民币陆仟零零柒元壹角肆分'
print(re.sub("零+", "0", s))
print(s.replace(r"零零", "0"))
x = '1111222bbb'
print(x.replace("2+", "0"))
print(x)
print(int('00'))
print('abc'.ljust(8, '0'))