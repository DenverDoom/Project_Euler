f = open("Problem13.txt", "r")
sumFull = 0
for x in f:
  x_long = int(x)
  sumFull = sumFull + x_long

sumFull_str = str(sumFull)
firstTenDigits = sumFull_str[0:10]

print(firstTenDigits)