def maxProfit(prices):
    max_profit = 0
    min_value = prices[0]
    for i in range(len(prices)):
        if prices[i] < min_value:
            min_value = prices[i]

        if prices[i] - min_value > max_profit:
            max_profit = prices[i] - min_value
    
    return max_profit

print(maxProfit([1,2]))