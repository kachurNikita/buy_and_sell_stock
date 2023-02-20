

# Best time to buy and sell stock

prices = [10, 5, 3, 6, 9, 11]

def max_profit(prices):
    buy, sell, profit = 0, 1, 0
    while sell < len(prices):
        current_profit = prices[sell] - prices[buy]
        if prices[buy] < prices[sell]:
            profit = max(profit, current_profit)
        else:
            buy = sell
        sell += 1
    return profit



print(max_profit(prices))