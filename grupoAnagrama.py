strs = ["act", "pots", "tops", "cat", "stop", "hat"]

anagrams = {}

for word in strs:
    sorted_word = "".join(sorted(word))
    if sorted_word not in anagrams:
        anagrams[sorted_word] = []
    anagrams[sorted_word].append(word)

lista = list(anagrams.values())

print(lista)