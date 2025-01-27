# Deve ter pelo menos 8 caracteres.
# Deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (!, @, #, etc.).
# Não deve conter espaços em branco.

senhaDigitada = str(input("Digite sua senha: "))


def verificaTamanho(senhaDigitada):
    if len(senhaDigitada) >= 8:
        return True
    return False


def verificaMaiuscula(senhaDigitada):
    for i in senhaDigitada:
        if i.isupper():
            return True    
    return False

def verificaMinuscula(senhaDigitada):
    for i in senhaDigitada:
        if i.islower():
            return True    
    return False

def verificaNumero(senhaDigitada):
    for i in senhaDigitada:
        if i.isnumeric():
            return True
    return False

def verificaCaractereEspecial(senhaDigitada):
    caracteres_especiais = "!@#%&*"
    if not any(c in caracteres_especiais for c in senhaDigitada):
        print("É necessário ao menos um caractere especial (!, @, #, etc.)")
        return False
    return True

def verificaCaractereBranco(senhaDigitada):
    for i in senhaDigitada:
        if i == " ":
            return False
    return True


if(
    verificaTamanho(senhaDigitada)
    and verificaMaiuscula(senhaDigitada)
    and verificaMinuscula(senhaDigitada)
    and verificaNumero(senhaDigitada)
    and verificaCaractereEspecial(senhaDigitada)
    and verificaCaractereBranco(senhaDigitada)
):
    print("senha válida")

else:
    print("Senha inválida")





