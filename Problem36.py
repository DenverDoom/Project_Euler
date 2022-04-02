def decTobin(n):
    return int(bin(n).replace("0b",""))
    
def isPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return True if temp==rev else False

sums=0
for i in range(1000000):
    if isPalindrome(i)==True and isPalindrome(decTobin(i))==True:
        sums+=i

print(sums)