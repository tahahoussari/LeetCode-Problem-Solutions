def maxEnergyBoost(energyDrinkA, energyDrinkB):
    n = len(energyDrinkA)
    f = [[0]*2 for _ in range(n)]
    f[0][0] = energyDrinkA[0]
    f[0][1] = energyDrinkB[0]
   
    for i in range(1, n):
        f[i][0] = max(f[i-1][0] + energyDrinkA[i], f[i-1][1])
        f[i][1] = max(f[i-1][1] + energyDrinkB[i], f[i-1][0])
    return max(f[n-1])


print(maxEnergyBoost([1,3,1], [3,1,1]))
print(maxEnergyBoost([4,1,1], [1,1,3]))
print(maxEnergyBoost([3,3,3], [3,4,6]))
print(maxEnergyBoost([5,5,6,3,4,3,3,4], [5,3,3,4,4,6,6,3]))