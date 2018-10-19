s=1.0
for i in range(1,366):
    if i%7 in[4,5,6,0]:
        s=s*1.01
print("365天后的能力值为{:.2f}".format(s))
