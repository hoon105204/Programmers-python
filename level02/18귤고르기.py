tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 4
tempList = set(sorted(tangerine,reverse=True)[:k])
print(sorted(tangerine,reverse=True)[:k])
print(len(tempList))
