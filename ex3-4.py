a=input("请输入一个五位数:")
if(a[0]==a[4])&(a[1]==a[3]):
    print("{}是回文".format(a))
else:
    print("{}不是回文".format(a))
