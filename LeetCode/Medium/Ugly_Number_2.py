#COMPLETED
def nthUglyNumber(n):
    uglyNumbers = [1] * n
    
    if n == 1:
        return 1

    p2 = 0
    p3 = 0
    p5 = 0

    for i in range(1, n):
        next2 = 2 * uglyNumbers[p2]
        next3 = 3 * uglyNumbers[p3]
        next5 = 5 * uglyNumbers[p5]

        uglyNumbers[i] = min(next2, next3, next5)

        if uglyNumbers[i] == next2:
            p2 += 1
        if uglyNumbers[i] == next3:
            p3 += 1
        if uglyNumbers[i] == next5:
            p5 += 1

    return uglyNumbers[-1]



print(nthUglyNumber(10))
print(nthUglyNumber(11))
print(nthUglyNumber(15))
print(nthUglyNumber(17))