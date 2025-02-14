def addTwoNumbers(l1, l2):
    ranges = min([l1,l2], key=len)
  
    numbersSum = []
    for i in range(len(ranges)):
        num = l1[i] + l2[i]
        if num > 10:
            remainder = num%10
        
        numbersSum.append((l1[i] + l2[i])%10)
        print((l1[i] + l2[i])%10)
    return numbersSum

print(addTwoNumbers([2,5,3],[5,6,4]))