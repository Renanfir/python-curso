class Camera:
    def __init__(self, nome, filmando = False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} ja está filmando")
            return
        print("Começou a filmar")
        self.filmando = True

    def para_filmar(self):
        if self.filmando == False:
            print(f"{self.nome} não estava filmando")
            return
        print(f"{self.nome} Parando de gravar")
        self.filmando = False

    def fotografa(self):
        if self.filmando:
            print(f"{self.nome} Não pode fotografar enquando filma")
            return
        print(f"{self.nome} Fotografando")


c1 = Camera('canon')


c1.filmar()
c1.para_filmar()
c1.fotografa()