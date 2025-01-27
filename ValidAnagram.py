s = "racecar"
t = "carrace"

s = sorted(s)
t = sorted(t)

if s == t and len(t) == len(s):
    print('True')
    print(s, t)
else:
    print("False")
    print(s, t)



