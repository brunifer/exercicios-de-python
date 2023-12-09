palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True: 
    letra_digitada = input('Digite a sua letra: ')
    tentativas += 1

    while len(letra_digitada) > 1:
        print('Digite somente uma letra por vez. ')
        letra_digitada = input('Digite a sua letra: ')
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    if palavra_formada == palavra_secreta:
        print(f'Parabéns, você acertou depois de {tentativas} tentativas.')
        break
    print(palavra_formada)
