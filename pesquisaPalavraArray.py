arr = ["Leão", "Tigre", "Elefante", "Girafa", "Cachorro", "Gato", "Coelho", "Panda", "Águia", "Tubarão"]
def pesq(palavra):
    for i in arr:
        if i == palavra:
            print(arr.index(i))


pesq("Tigre")