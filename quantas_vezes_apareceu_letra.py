frase = 'O Python é uma linguagem de programação multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'.lower()

indice = 0
apareceu_mais_vezes = 0
letra = ''

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == ' ':
        indice += 1
        continue

    quantas_vezes_apareceu = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_apareceu:
        apareceu_mais_vezes = quantas_vezes_apareceu
        letra = letra_atual

    indice += 1

print(f'A letra que apareceu mais vezes foi {letra} '
      f'e foi encontrada {apareceu_mais_vezes} vezes.')
print(frase)