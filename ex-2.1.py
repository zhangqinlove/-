SymbolStr=input("请输入带有符号的温度值:")
if SymbolStr in ['F','f']:
    t=(eval(input("请输入带有符号的温度值:")))
    C=int((t-32)/1.8)       
    print("转换后的温度值是{}C".format(C))
elif SymbolStr in ['C','c']:
    t=eval(input("请输入带有符号的温度值:"))
    F=int(t*1.8+32)
    print("转换后的温度值是{}F".format(F))
else:
    print("输入格式错误")
          
