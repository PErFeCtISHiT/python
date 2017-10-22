'''result = 0
for i in range(1,5):
    for j in range (1,5):
        for k in range (1,5):
            if i != j and j != k and k != i:
                print (i * 100 + j * 10 + k)
                result+=1
print(result)
i = int(input("input"))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        i = arr[idx]
print(r)
def f(a):
    for i in range(a + 1):
        if i * i == a:
            return True
    return False
x = -99;
while True:
    if f(x + 100) and f(x + 268):
        print(x)
        x += 1
    else:
        x += 1
    if x > 2000:
        break
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
isSpecial = False
def isSp(y):
    ret = False
    if y % 100 == 0 and y % 400 == 0:
        ret = True
    elif y % 4 == 0:
        ret = True
    return ret
days = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    ret = days[month - 1]
else: print("error")
ret += day
if isSp(year) and month > 2:
    ret += 1
print("result : " + str(ret))'''
def qsort(list,start,end):
    