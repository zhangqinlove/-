def isNum(s):
    try:
        n=eval(s)
    except:
        return False
    return True
s=input("请输入字符串:")
if isNum(s):
    print("{}是数字".format(s))
else:
    print("{}不是数字".format(s))
