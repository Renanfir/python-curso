import os
import shutil

#Criação das variáveis com caminhos
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'C:\\Users\\User\\TESTES_RENAN')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

#Verificação e criação de pasta
os.makedirs(NOVA_PASTA, exist_ok=True)

# Pondo cada diretorio de uma pasta em outra
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        #Verificação e criação de pasta
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)
    
    # Pondo cada arquivo de uma pasta em outra
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)

