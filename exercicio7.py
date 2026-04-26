# esse codigo calcula o preco da viagem com base na distancia que será percorrida.
distancia = float(input("Digite a distancia da viagem: "))

if distancia <= 200: 
    preco = distancia * 0.50
    print(f"O valor da viagem custará R${preco}.")

else: 
    preco = distancia * 0.40
    print(f"O valor da viagem custará R${preco}")

