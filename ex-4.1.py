p = 7
count = 0;
while True:
    n = eval(input('请输入一个0-9之间的整数：'))
    count += 1
    if n > p:
        print('遗憾，太大了')
    elif n<p:
        print('遗憾，太小了')
    else:
        break
print('预测{}次，你猜中了！'.format(count))
        
