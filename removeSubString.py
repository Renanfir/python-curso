def sub(completo, *args):
    for i in args:
        completo = str(completo).replace(i,"").strip()
        completo = " ".join(completo.split())
    print(completo)

sub("Vontade de comer pão com banana", "pão","banana", "Vontade")

