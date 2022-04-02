x=100
count=0
for i in range(2,x):
    res=0
    num=i
    while(num!=0):
        rem=num%10
        res+=rem*rem
        num=num//10
        if res!=89:
            num=res
        else:
            count=count+1
print(count)