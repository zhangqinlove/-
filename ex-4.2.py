O=input("请输入一行字符:")
alphabet=0
number=0
space=0
other=0
for c in O:
    if 'A'<=c<='Z' or 'a'<=c<='z':
        alphabet+=1
    elif c==' ':
        space +=1
    elif '0'<=c<='9':
        number+=1
    else:
        other+=1
print("此行中有{}个字母，有{}个空格,有{}个数字，有{}个其他字符。".format(alphabet,space,number,other))
