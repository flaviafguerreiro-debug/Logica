# Projeto 5 - Calculadora Melhorada com validação

def somarmultiplosnumeros(numeros):
    # Se a lista estiver vazia, devolve 0
    if not numeros:
        return 0
    soma = 0
    for n in numeros:
        if isinstance(n, (int, float)):
            soma += n
        else:
            raise ValueError("A lista deve conter apenas números")
    return soma

def multiplicarmultiplosnumeros(numeros):
    # Se a lista estiver vazia, devolve 1 (neutro da multiplicação)
    if not numeros:
        return 1
    produto = 1
    for n in numeros:
        if isinstance(n, (int, float)):
            produto *= n
        else:
            raise ValueError("A lista deve conter apenas números")
    return produto

def ehinteiro(numero):
    if not isinstance(numero, (int, float)):
        raise ValueError("O valor deve ser um número")
    return isinstance(numero, int) or numero.is_integer()

def ehpar(numero):
    if not isinstance(numero, (int, float)):
        raise ValueError("O valor deve ser um número")
    return ehinteiro(numero) and numero % 2 == 0

# Testes para ver as funções funcionando
lista = [2, 5, 3.5, -1]
print("Soma:", somarmultiplosnumeros(lista))
print("Multiplicação:", multiplicarmultiplosnumeros(lista))
print("É inteiro 4.2?", ehinteiro(4.2))
print("É inteiro -6?", ehinteiro(-6))
print("É par 8?", ehpar(8))
print("É par 2.5?", ehpar(2.5))
print("Lista vazia soma:", somarmultiplosnumeros([]))
print("Lista vazia multiplicação:", multiplicarmultiplosnumeros([]))

















































































    



