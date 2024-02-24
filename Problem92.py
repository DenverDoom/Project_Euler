def end_square_sum(num):
    num_str = str(num)
    print(num_str)
    result = False
    while(num != 0):
        sum = 0
        for i in num_str:
            sum = sum + int(i)*int(i)
        if(sum == 89):
            result = True
            num = 0
            break
        elif(sum == 1):
            result = False
            num = 0
            break
        else:
            num_str = str(sum)

    return result

limit = 10000000
count = 0
for i in range(1,limit):
    if (end_square_sum(i) == True):
        count+=1

print(count)