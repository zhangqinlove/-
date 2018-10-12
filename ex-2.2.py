#e TempCovert.py
Currency=input("请输入带有符号的货币值:")
if Currency[-1] in ['R','r']:
    U=(eval(Currency[0:-1])/6)
    print("转换后的货币值是USD{:.2f}U".format(U))
elif Currency[-1] in ['U','u']:
    R=(eval(Currency[0:-1])*6)
    print("转换后的货币值是RMB{:.2f}R".format(R))
else:
    print("输入格式错误")
       
       
