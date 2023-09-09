valido = False
while not valido:  # validação do tipo de dados. 
    try: # para que o programe não pare ao inserir um dado do tipo difernte de 'float'(ValueError)

# Variáveis 
        peso = float(input('Digite seu peso:'))
        altura = float(input('Digite sua altura:'))

        if type(peso) == float and type(altura) == float:
            valido = True
    except ValueError: # caso o erro ValueError ocorra, o programa não para e sim exibe uma mensagem e volta ao loop
        print('Dados inserido inválidos. Só números são aceitos! \n <Tente Novamente> \n ---------------- ')

# prcessamento de dados

resultado = peso/altura**2

# Saída de dados

print("-"*20)
print('Resultado do seu IMC:')

if resultado < 18.5:
    print('Abaixo do peso')
elif 18.6 < resultado <= 24.9:
    print('Peso ideal')
elif 25.0 < resultado <= 29.9:
    print('Levemente acima do peso')
elif 30.0 < resultado <= 39.4:
    print('Obesidade grau I')
elif 35.0 < resultado <= 39.9:
    print('Obesidade grau II - severa')
elif resultado >= 40.0:
    print('Obesidade grau III - morbida - Você vai morer ')
print('resultado: {:.2f}'.format(resultado))



