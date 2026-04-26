nome = str(input("digite seu nome completo: ")).strip()
# a funcao strip foi utlizada para remover os espacos das frase para nao ser contadas.
print("seu nome em maiusculo é",nome.upper())
print("seu nome em minusculo é",nome.lower())
print("seu nome tem",len(nome) - nome.count(" "),"letras")
