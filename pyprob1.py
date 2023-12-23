l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
for i in range(0,len(l1)):
    if i%2!=0:
        l3=[]
        l3.append(l1[i])
for i in range(0,len(l2)):
    if i%2==0:
        l4=[]
        l4.append(l2[i])
l3.extend(l4)
print(l3)

result = 1
for i in zip(l1,l2):
    result = 1*i

print(result)