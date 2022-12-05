a = 'Possible'
b = 'Not Possible'
N= int(input("Input number: "))
# Condition for cutting the cake into n equal pieces	
if 360 % N == 0:
    print(a)
else:
    print(b)
# condition for cutting the cake into N pieces of any size
if N <360:
    print(a)
else:
    print(b)
# condition for cutting the cake into N pieces such that no two of them are equal
if N <26:
    print(a)
else:
    print(b)
