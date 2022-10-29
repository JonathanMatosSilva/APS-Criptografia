def expansaoTexto(texto):
    #  Expansão de texto para 128 bytes
    txt = texto + '{' * (128 - len(texto))
    return txt

def expansaoChave(chave):
    #  Expansão de chave para 128 bytes
    key = chave + '}' * (128 - len(chave))
    return key

def reducaoString(txt):
    for x in txt:
        if x == '{':
            txt = txt.replace('{',"")
    return txt

def paraBinario(txt):
    """Converte texto para binarios"""

    valores_individuais, valores_binarios = [], []

    for letra in txt:
        valores_individuais.append(ord(letra))
    for letra in valores_individuais:
        valores_binarios.append(bin(letra)[2:])
    binario = []
    for i in valores_binarios:
        binario.append(i.zfill(8))
    return binario

def paraString(binario):
    """Coverte binarios para string"""
    partes = []
    for index in range(0, len(binario), 8):
        partes.append(binario[index : index + 8])
    string = ''
    for i in partes:
        decimal = int(i, 2)
        string = string + chr(decimal)
    return string

def bin_xor(binario, chave):
    #  Xor binario-chave
    cifrado = ''
    for x,y in zip(binario, chave):  # Percorre cada posição da lista de binarios.
        for i,j in zip(x, y):  # Percorre cada posição de binarios individualmente.
            xor = int(i) ^ int(j)  # Calcula o xor
            cifrado = cifrado + str(xor)  # Concatena o resultado
    return cifrado
    
def xor_bin(xor, chave):
    #  Xor chave-binario
    partes = []
    for index in range(0, len(xor), 8):
        partes.append(xor[index : index + 8])
    decifrado = ''
    for x,y in zip(partes, chave):  
        for i,j in zip(x, y):  
            bin = int(i) ^ int(j)  
            decifrado = decifrado + str(bin)  
    partes = []
    return decifrado

def linha(tam=42):
    return "-" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


while True:
    resposta = menu(['Codificar', 'Decodificar', 'Sair'])
    
    if resposta == 1:
        #  Expandir chave e texto para 128 bytes
        texto = expansaoTexto(input('Digite o seu texto: '))
        chave = expansaoChave(input('Digite sua chave: '))
        #  Conversão para binario
        bin_texto = paraBinario(texto)
        bin_chave = paraBinario(chave)
        #  Calculo xor
        texto_codificado = bin_xor(bin_texto, bin_chave)
        print(f'\033[34mTexto codificado:\033[0m {texto_codificado}')
    elif resposta == 2:
        texto_codificado = input('Digite o texto codificado: ')
        # Expansão da chave para 128 bytes
        chave = expansaoChave(input('Digite sua chave: '))
        #  Conversão da chave para binario
        bin_chave = paraBinario(chave)
        #  Reverte o calculo xor
        bin_texto = xor_bin(texto_codificado, bin_chave)
        #  Conversão para string
        texto = paraString(bin_texto)
        #  Redução da string
        texto = reducaoString(texto)
        print(f'\033[34mTexto original:\033[0m {texto}')
    elif resposta == 3:
        print('\033[34mAté mais...\033[0m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
