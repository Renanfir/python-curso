import time
from tkinter import *
from PIL import Image, ImageTk

def criar_janela():
    root = Tk()
    root.title('Beber agua')
    root.geometry("500x500")

    def piscar_tela():
        cor_atual = root.cget("bg")
        nova_cor = "red" if cor_atual == "#F4F4F4" else "#F4F4F4"
        root.config(bg=nova_cor)
        root.after(500, piscar_tela)

    root_label = Label(root, text="Beber água", font=("Helvetica", 35))
    root_label.pack(pady=20)

    piscar_tela()
    root.mainloop()

while True:
    criar_janela()  
    time.sleep(600)  
