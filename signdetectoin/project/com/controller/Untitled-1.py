
global count 
count = 0
n = 1012
for i in str(n):
    print (i)
    if int(i)!=0:
        i = int(i)
        if n%i == 0:
            count = count + 1
print (count)