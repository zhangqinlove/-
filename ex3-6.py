import time
scale=50
t=time.clock()
for i in range(scale+1):
    a=","*i
    c=(i/scale)*100
    t=time.clock()
    print("\rstarting{:^3.0f}%[{}]{:.2f}s Done".format(c,a,-t))
    time.sleep(0.05)
