lim = int(input())
vals = []
print(lim)
for l in range(lim):
    vals.append(int(input()))
dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in dict:
    for j in vals:
        if j%i==0:
            dict[i]+=1
print(dict)
