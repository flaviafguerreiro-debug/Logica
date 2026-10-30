nomes_aprovados = ["João", "Maria", "Pedro", "Mariana" ]

nome = input("Digite seu nome: ").strip()

#.strip() remove espaços em branco no início e no final da string digitada pelo usuário.

if nome. lower() in [n.lower() for n in nomes_aprovados]:
    print(f"{nome} aprovado!")
else:
    print(f"{nome} reprovado!")

#.lower() transforma a string em letras minúsculas, para que a comparação seja feita de forma case-insensitive.
# colocando o nome da lista aparece aprovado / se for diferente aparece reprovado.

