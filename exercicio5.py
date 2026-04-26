# esse codigo confere se voce esta no limite de velocidade permitido pela via
# caso nao esteja o motorista sera multado em R$7,00 por km fora do limite permitido.
velocidade = float(input("digite a velocidade atual do carro: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"voce foi multado em R${multa:.2f}!")
else: 
    print("voce esta dentro do limite de velocidade da via")
