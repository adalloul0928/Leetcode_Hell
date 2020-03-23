def finalPrice(prices):
    fullPrice = []
    stackMin = []
    cost = 0

    for i in reversed(range(len(prices))):
        while stackMin and stackMin[-1] > prices[i]:
            stackMin.pop()
        if stackMin:
            cost += prices[i] - stackMin[-1]
        else:
            cost += prices[i]
            fullPrice.append(i)
        stackMin.append(prices[i])
    print(cost)
    fullPrice.sort()
    print(*fullPrice)

input = [1, 3, 3, 2, 5]
print(finalPrice(input))