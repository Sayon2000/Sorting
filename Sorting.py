from array import *
vals  = array('I',[5,3,2,15,256,45,1])

for i in range(len(vals)-1):
    for j in range(len(vals)-i-1):
        if vals[j]> vals[j+1]:
            vals[j] = vals[j]+vals[j+1]
            vals[j+1] = vals[j] - vals[j + 1]
            vals[j] = vals[j] - vals[j + 1]

for e in vals:
    print(e)