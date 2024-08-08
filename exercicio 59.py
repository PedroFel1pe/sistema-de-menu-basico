escolha = 0
num1 = int(input('informe um valor:'))
num2 = int(input('informe um valor:'))
while escolha != 5:
    print('Veja as opções:')
    print('[1] somar')
    soma = num1 + num2
    print('[2] multiplicar')
    multiplicar = num1 * num2
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair')
    escolha = int(input('Qual opção escolheu?'))
    if escolha == 1:
        print(f'a soma de {num1} + {num2} é {soma}.')
    elif escolha == 2:
        print(f'a multiplicação de {num1} * {num2} é {multiplicar}.')
    elif escolha == 3:
        if num1 > num2:
            print(f'o maior numero entre {num1} e {num2} é {num1}')
        else:
            print(f'o maior numero entre {num1} e {num2} é {num2}')
    elif escolha == 4:
        num1 = int(input('informe um valor:'))
        num2 = int(input('informe um valor:'))
