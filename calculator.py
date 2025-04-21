'''
Crie uam claculadora interativa que:
Solicita dois números pro usuário
Mostrta um menu de operações disponíveis:
SOMA +
SUBTRAÇÂO -
MULTIPLICAÇÃO *
DIVISÃO /
POTÊNCIA **
DIVISÃO INTEIRA //
RESTO DA DIVISÃO %

O Usuario escolhe a o peração e a calculadora retorna o resultado 
Ao final, pergunta se o usuário quire fazer outra operação ou sair 

'''

print(20*"-" , "CALCULADORA COMPLETA" ,20*"-") #Mostrando o titulo 

def ler_numero(mensagem):# definindo a função ler número que vai ler o número recebido
    while True:
        entrada=input(mensagem).replace(",",".")
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número inteiro ou com vírgula/ponto.  ")
n1=ler_numero("Digite o primeiro número: ")
n2=ler_numero("Digite o segundo número:  ")
while True:
    print(20 * "-", " MENU DE OPERAÇÕES DISPONIVEIS" ,20 * "-")
    print("[1] +(SOMA)")
    print("[2] -(SUBTRAÇÃO)")
    print("[3] *(MULTIPLICAÇÃO)")
    print("[4] /(DIVISÃO)")
    print("[5] **(POTÊNCIA)")
    print("[6] //(DIVISÃO INTEIRA")
    print("[7] % (RESTO DA DIVISÃO)")
    print("[8] (SAIR DO PROGRAMA)")

    opcao=int(input("Escolha uma das opções do menu: "))
    if opcao<1 or opcao>8:
        print("Opção invailda. Tente novamente. ")
        continue
    if opcao==1:
        soma=n1+n2
        print(f"{n1} + {n2} = {soma}")
    elif opcao==2:
        subtracao=n1-n2
        print(f"{n1} - {n2} = {subtracao}")
    elif opcao==3:
        multi= n1*n2
        print(f"{n1} * {n2} = {multi}")
    elif opcao==4:
        divisao = n1/n2
        if n2 != 0:
            print(f"{n1} / {n2} = {divisao}")
        else:
            print("ERRO: Divisão por zero!!")
    elif opcao==5:
        potencia=n1**n2
        print(f"{n1} ** {n2} = {potencia}")
    elif opcao==6:
        diviint=n1//n2
        if opcao!=0:
            print(f"{n1} // {n2} = {diviint}")
        else:
            print("ERRO: Divisão por zero!!")
    elif opcao==7:
        restodiv= n1%n2
        if n2!=0:
            print(f"{n1} % {n2}= {restodiv}")
        else:
            print("ERRO: Divisão por zero!!")
    else:
        opcao==8
        print("Saindo do programa...")
        print("FOI UM PRAZER TE AJUDAR :)")
        break
            