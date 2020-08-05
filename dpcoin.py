def dpMakeChange(coinValueList, change, minCoin, coinUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoin[cents - j] + 1 < coinCount:
                coinCount = minCoin[cents - j] + 1
                newCoin = j
        minCoin[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoin[change]
def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


print(dpMakeChange([1,5,10,21,25],63,[0]*64,[0]*64))