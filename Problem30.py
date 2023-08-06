max_digits = 6
upper_bound = max_digits * pow(9,5)
lower_bound = 10
num_list = []

def powSum(n):
    s = str(n)
    sumP = 0
    for i in s:
        sumP = sumP + pow(int(i),5)
    return sumP

for i in range (lower_bound,upper_bound+1):
    if(i == powSum(i)):
        num_list.append(i)

print(sum(num_list))