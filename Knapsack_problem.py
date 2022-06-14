def knapsack_dp(capacity, weights, values, n):
    grid = [[0 for x in range(capacity + 1)]
            for x in range(n+1)]
    for item in range(n+1):
        for cap in range(capacity+1):
            if item == 0 or cap==0:
                grid[item][cap]=0

            elif weights[item-1] <=cap:
                grid[item][cap] = max(values[item-1] + grid[item -1][cap-weights[item-1]], grid[item-1] [cap])

            else:
                grid[item][cap] = grid[item-1][cap]

    return grid[n][capacity]

item_val=[3000, 2000, 1500]
item_wt=[4,3,1]
total_cap=4
n_items = len(item_val)

print('Max value to put in knapsack of capacity W: ')
print(knapsack_dp(total_cap, item_wt, item_val, n_items), '$')