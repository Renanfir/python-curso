sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

ranges = []
for i in sentences:
    ranges.append(len(i.split()))

# for i in splitado:
#     print(i, len(i))
print(max(ranges))