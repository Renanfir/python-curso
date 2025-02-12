boxes = "110"
vazio = []
if len(boxes) == 1:
    # return [0]
    ...
if boxes.count('1') == 0:
    for i in boxes:
        vazio.append(int(i))
    # return vazio

grupo = []
ums = 0
for i in range(len(boxes)):
    for j in range(len(boxes)):
        if boxes[j] == '1':
            grupo.append(abs(j - i))
            

# return ([sum(grupo[i:i+boxes.count('1')]) for i in range(0, len(grupo), boxes.count('1'))])
