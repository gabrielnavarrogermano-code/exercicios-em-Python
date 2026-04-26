# esse codigo calcula qual a porcentagem de aumento com base no seu salario atual.
salario = float(input("digite seu salario atual: "))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
    print(f"seu novo salario será de R${novo_salario:.2f}.")

else:
    novo_salario = salario + (salario * 0.10)
    print(f"Seu novo salário será de R${novo_salario:.2f}.")
