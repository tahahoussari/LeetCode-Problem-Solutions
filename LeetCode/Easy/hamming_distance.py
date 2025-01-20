def hammingDistance(x, y):
    binary_x = bin(x)[2:].zfill(100)
    binary_y = bin(y)[2:].zfill(100)
    count = 0
    for i in range(len(str(binary_x))):
        if binary_x[i] != binary_y[i]:
            count += 1

    return count

print(hammingDistance(1,4))
print(hammingDistance(3,1))