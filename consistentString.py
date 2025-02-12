allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
qtd = 0
for i in allowed:
    for j in range(len(words)):
        words[j] = words[j].replace(i,"")

for i in words:
    if i == '':
        qtd += 1 
        

print(qtd)