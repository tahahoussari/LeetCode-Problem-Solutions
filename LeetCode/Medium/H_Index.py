#COMPLETED
def hIndex(citations):
    indexH = 0
    if len(citations) == 1:
        if citations[0] == 0:
            return 0
        else:
            return 1

    citations.sort()
    for i in range(len(citations)):
        count = 0

        if citations[i] != 0:
            numCit = citations[i]
            count += 1
            for j in range(i+1, len(citations)):
                if citations[j] >= numCit:
                    count += 1
            if count > indexH and count <= citations[i]:
                indexH = count
            elif count > indexH and citations[i] > indexH:
                indexH = citations[i]


    return indexH


print(hIndex([3,0,6,1,5]))
print(hIndex([2,3,2]))
print(hIndex([0,0,2]))
print(hIndex([2,1,1,2]))
print(hIndex([0,3,2,0]))