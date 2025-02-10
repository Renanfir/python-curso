jewels = "aA"
stones = "aAAbbbb"
qtd = 0
for i in jewels:
    qtd += stones.count(i)
print(qtd)