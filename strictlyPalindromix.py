n = 9
b = 2
m = n
resultado = True
for i in range(b, m - 1):
    result = []

    while m != 0:
        result.append(str(m % b))
        m //= b 

    numero_convertido = "".join(result[::-1])
    m = n
    b += 1
    print(numero_convertido, numero_convertido[::-1])
    if numero_convertido != numero_convertido[::-1]:
        resultado = False
        break
# return resultado
    








# while m != 0:
#         result.append(str(m%b))
#         m = round(m/b)
#         if m == 0:
#             result = "".join(result)
#             if result == result[::-1]:
#                 print("true")
#             else:
#                 print("false")