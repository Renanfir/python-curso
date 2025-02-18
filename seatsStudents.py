seats = [12,14,19,19,12]
students = [19,2,17,20,7]

moves = 0

for i,j in zip(sorted(seats), sorted(students)):
    moves += abs(i - j)

print(seats,students,moves)


