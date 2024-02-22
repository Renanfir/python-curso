cidade = ['Salvador', 'Ubatuba', 'Belo horizonte']
estado = ['BA', 'SP', 'MG']

# Calculando o intervalo_maximo com o tamanho das palavras
intervalo_maximo = min(len(cidade), len(estado))

# Concatenando
def concatenador(cid, est):
    return [
        (cid[i] + "," + est[i]) for i in range(intervalo_maximo)
    ]

# Saída
print(concatenador(cidade, estado))
