def has_path_sum(root, targetsum):
    sum = 0
    for i in root:
        if i != None:
            if targetsum - i > 0:
                sum += i
                targetsum -= i
            if targetsum == 0:
                return True
        
    return False

print(has_path_sum([5,4,8,11,None,13,4,7,2,None,None,None,1], 22))