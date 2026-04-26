# esse codigo calcula a media de um aluno 
n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite sua segunda nota:"))
media = (n1 + n2)/2

print(f"A sua media é de {media:.1f}")

if media >= 6.0:
    print("parabéns, voce atingiu a media.")
else:
    print("voce está de recuperacao")

