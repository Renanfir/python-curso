s = "abc"
t = "bac"
result = 0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            result += abs((i - j))

print(result)

