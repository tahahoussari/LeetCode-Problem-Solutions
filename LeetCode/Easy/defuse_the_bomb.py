def decrypt(code, k):
    decrypted_code = []
    if k == 0:
        for i in range(len(code)):
            decrypted_code.append(0)
    
    if k > 0:
        j = 0
        sum = 0
        for i in range(k+1):
            index = i+1
            while j < k:
                if index > k:
                    index = 0

                sum += code[index]       
                j += 1
                index += 1

            decrypted_code.append(sum)
            sum = 0
            j = 0

    if k < 0:
        j = 0
        sum = 0
        for i in range(k):
            index = i+1
            while j < k:
                if index > k:
                    index = len(code)
                
                sum += code[index]  
            decrypted_code.append(sum)
            sum = 0
            j = 0

    return decrypted_code


print(decrypt([1,2,3,4], 0))
print("------------------------------------")
print(decrypt([5,7,1,4], 3))
print("------------------------------------")
print(decrypt([2,4,9,3], -2))