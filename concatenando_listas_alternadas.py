cidade = ['Salvador','Ubatuba','Belo horizonte']
estado = ['BA','SP','MG']

intervalo_maximo = min(len(cidade), len(estado))

def concatenador(cid,est):
    return[
        (cid[i] +","+ est[i]) for i in range(intervalo_maximo)
        ]


print(concatenador(cidade,estado))