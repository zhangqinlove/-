a=47.5
for i in range(10):
    a=a+0.5
    b=a*(1+0.165)
    print("地球体重为{:.2f},月球体重为{:.2f}.".format(a,b))
