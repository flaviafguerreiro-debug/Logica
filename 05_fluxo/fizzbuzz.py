
for n in range (1, 1001): # O laço 'for' percorre os números de 1 a 1000. 
     # A variável 'n' assume o valor de cada número a cada volta do laço.
    if n % 15  == 0:
        # Verifica PRIMEIRO se é múltiplo de 15 (ou seja, de 3 e 5 ao mesmo tempo).
    # Se for, imprime "FizzBuzz" e o 'elif' abaixo é ignorado.
      
        print("FizzBuzz")
    elif  n % 5 == 0: 
        # Se não foi 15, verifica se é múltiplo de 5.
        print ("Buzz")
    elif n % 3 == 0:
        # Se não foi 15, verifica se é múltiplo de 3.
        print ("Fizz")
    else: # Se não atendeu nenhuma das condições acima, imprime o próprio número.
        print(n)




