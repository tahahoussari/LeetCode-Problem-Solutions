def hammingWeight(n):
    num_1s = 0
    binary_n = bin(n)
    for i in binary_n:
        if i == "1":
            num_1s += 1
    return num_1s


print(hammingWeight(11))
print(hammingWeight(128))
print(hammingWeight(2147483645))