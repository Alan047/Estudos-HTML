validacao = False

while not validacao:
    try:
        dado1 = float(input('numero'))
        if type(dado1) == float:
            validacao = True




    except ValueError:
        print('erro de dados')

        
print('fim do programa')
