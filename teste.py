import datetime



def quantos_acima_media(lista):
    media = sum(lista) /len(lista)
    soma = 0
    for i in lista:
        if i> media:
            soma+=1
    return soma

def start_with_a(lista):
    quantidade = 0
    for i in lista:
        if i[0] == "a":
            quantidade +=1
    return quantidade


def soma_indice_impar(lista):
    soma = 0
    for i in range(len(lista)):
        if i%2 !=0:
            soma += lista[i]
    return soma

def substituir(lista):
    nova_lista =[]
    for i in lista:
        split = list(i)
        split[0] = "a"
        nova = "".join(split)
        nova_lista.append(nova)
    return nova_lista
        

def modificar_string(entrada):
    #1
    entrada = entrada.strip()
    #2
    #substitua a vírgula por um ponto de exclamação
    
    entrada = entrada.replace(",","!")
    # (3) substitua “olá” por uma saudação
    hora = datetime.datetime.now().hour
    if hora <12:
        entrada = entrada.replace("Olá","Bom dia")
    elif hora<18:
        entrada = entrada.replace("Olá","boa tarde")
    else:
        entrada = entrada.replace("Olá","boa noite")


    return entrada


teste = " Olá usuário, bem-vindo ao sistema  "

print(modificar_string(teste))


