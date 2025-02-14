import math

def maxDistance(position, m):
    distances = []
    numbers = []
    position.sort()
    if m == 2:
        return position[-1] - position[0]
    else:
        distances.append(position[-1] - position[0])
        jump = math.floor(len(position)/(m-1))
        for i in range(1,len(position)-1):
            distances.append(position[i])

    return distances


print(maxDistance([5,4,3,2,1,1000000], 2))
print(maxDistance([7,4,3,2,1], 3))