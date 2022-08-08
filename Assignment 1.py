primeNum = []

number=int(input("Enter Number: "))
def isPrime(j):
    i = 2
    while (i < j):
        if j % i == 0:
            return False
        i = i + 1
    return True


def printNum(l):
    r= 2
    while r <= l:
        if isPrime(r):
            primeNum.append(r)
        r= r + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

u = 0
while u< numOfPrime:
    sum += primeNum[g]
    u = u + 1

ans = sum / numOfPrime

print(ans)
