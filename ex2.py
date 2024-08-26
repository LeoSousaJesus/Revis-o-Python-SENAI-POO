# Programa avaliação Aprovado ou Reprovado
# Solicita as notas ao usuário e as converte para inteiros
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")


soma = nota1 + nota2 + nota3
print(f"Soma das notas: {soma:,2f}")

media = soma / 3
print(f"Média das notas: {media:.2f}")

if media>= 5:
    print("Aluno Promovido")
else:
    print("Aluno Retido")

