def countLargestGroup(n):
    count = 0
    groups = []

    for j in range(n):
        groups.append([])


    for i in range(1, n+1):
        sum = 0
        for c in str(i):
            sum += int(c)
        groups[sum-1].append(i)


    current_max = 0
    for i in range(len(groups)):
        if current_max == len(groups[i]):
            count += 1
        elif len(groups[i]) > current_max:
            current_max = len(groups[i])
            count = 1

    return count

print(countLargestGroup(13))
print(countLargestGroup(2))
print(countLargestGroup(24))