def isPowerOfTwo(n):
    for i in range(32):
        if (2**i) == n:
            return True
    return False

print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(3))