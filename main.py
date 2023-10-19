def dimensoesObjeto(): #primeira função criada para as dimensões do objeto
    while True: #criei um laço
        try: #utilizando 'try' e 'except' para tentar rodar o código caso o usário digitar um valor não numérico
            comprimento = float(input('Digite o comprimento do objeto (em cm):'))
            largura = float(input('Digite a largura do objeto (em cm):'))
            altura = float(input('Digite a altura do objeto (em cm):'))
            #variáveis acima criadas para receber as dimensões do objeto, utilizando float caso tenha ponto flutuante
            volume = comprimento * largura * altura #variável criada para receber o total das dimensões já somados em cm³
            print('O volume do objeto é (em cm³): {}'.format(volume))
            #condições criadas para retornar o valor do volume do objeto de acordo com a tabela do exercício
            if volume < 1000:
                return 10
            elif (volume >= 1000) and (volume < 10000):
                return 20
            elif (volume >= 10000) and (volume < 30000):
                return 30
            elif (volume >= 30000) and (volume < 100000):
                return 50
            else: #'else' utilizado caso a dimensão seja maior do que a permitida
                print('Não aceitamos objetos com dimensões tão grandes \n'
                      'Entre com as dimensões desejadas novamente ')
        except ValueError: #erro de valor não numérico
            print('Você digitou alguma opção do objeto com o valor não numérico')

def pesoObjeto(): #segunda função criada para receber peso do objeto
    while True: #criei um laço
        try: #utilizando 'try' e 'except' para tentar rodar o código caso o usário digitar um valor não numérico
            peso = float(input('Digite o peso do objeto (em kg):'))
            #variável criada para receber peso do objeto, 'float' utilizado para receber valor de ponto flutuante
            #condições criadas para retornar o multiplicador do peso de acordo com a tabela do exercício
            if peso <= 0.1:
                return  1
            elif (peso >= 0.1) and (peso < 1):
                return  1.5
            elif (peso >= 1) and (peso < 10):
                return  2
            elif (peso >= 10) and (peso < 30):
                return  3
            else: #'else' utilizado para caso o peso exceda o máximo permitido
                print('Não aceitamos objetos tão pesados \n'
                      'Por favor entre com o peso do objeto novamente')
                continue #volta para o início do laço para repetir a pergunta
        except ValueError:
            print('Você digitou peso do objeto com o valor não numérico \n'
                      'Por favor entre com o peso do objeto novamente')
            # '\n' que está sendo utilizado é para quebrar a linha quando aparecer na saída do console


def rotaObjeto(): #terceira função criada para receber rota do objeto
    while True: #criei um laço
        #variável pra receber a rota do objeto
        rota = input('Selecione a rota: \n'+
                     'RS - De Rio de Janeiro até São paulo \n'+
                     'SR - De São Paulo até Rio de Janeiro \n' +
                     'BS - De Brasília até São Paulo \n' +
                     'SB - De São Paulo até Brasília \n' +
                     '>>')
        #variável criada para caso o cliente digite em letra minúscula, o programa aumente a fonta automaticamente, '.upper()' utilizado para fazer isso
        rota = rota.upper()
        #condições criadas para receber o multiplicador de acordo com a rota
        if rota == 'RS':
            return 1
        elif rota == 'SR':
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'SB':
            return 1.2
        else: #'else' caso digitem rota não existente
            print('Você digitou uma rota que não existe \n'
                  'Por favor entre com a rota desejada novamente')
            continue #volta para o início do laço para repetir a pergunta

#início do programa
#print do meu nome e RU no console
print('Bem-vindo a companhia de logística da Galdina Silva de Souza RU:4370444')

#variáveis criadas para receber as funções criadas acima
dimensoes = dimensoesObjeto()
pesoKG = pesoObjeto()
rotaObj = rotaObjeto()

#variável criada para fazer a equação que foi pedida no exercício
total = dimensoes * pesoKG * rotaObj

#print final retornando o valor feito pela equação, e os valores de dimensão, peso, e rota que foram utilizados para realizar a conta
print('Total a pagar (R$) {:.2f} (Dimensões: {:.2f} * peso: {:.2f} * rota: {:.2f})' .format(total, dimensoes, pesoKG,rotaObj))
