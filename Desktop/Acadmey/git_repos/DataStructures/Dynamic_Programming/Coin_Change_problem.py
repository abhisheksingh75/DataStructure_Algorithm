
def coinChange(start, coins,  s, ans,):
    
    if  s == 0:
        print(ans)
        return 1 
    count = 0
    for i in range(start, len(coins)):
        if s >= coins[i]:
            ans.append(coins[i])
            val1 = coinChange(start, coins,  s-coins[i], ans)
            ans.pop()
            val2 = coinChange(start+1, coins,  s, ans)
            count += val1 +val2 
    return count

arr = [1, 2, 3] 
m = len(arr) 
ans = []
print(coinChange(0, arr, 4, ans)) 