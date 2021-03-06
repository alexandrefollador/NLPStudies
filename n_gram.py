lista = ['abacate', 'abacaxi', 'abobora', 'abobrinha', 'ananás', 'maça', 'mamão','manga', 'melancia', 'melão', 'mexerica', 'morango']

palavra = 'abacati'

def retorna_bigrama(word):
    tamanho = len(word)
    list = []
    for i in range(tamanho):
        j = i + 1
        if j < (tamanho):
            bigram = word[i] + word[j]
            list.append(bigram)
    bigrama = set(list)
    return bigrama

def remove(remA, remB, setLista):
    for item in remA:
        setLista.discard(item)
    for item in remB:
        setLista.discard(item)
    return setLista

a = len(retorna_bigrama(palavra))
big_palavra = retorna_bigrama(palavra)

dict = {}
for item in lista:
    big_lista = retorna_bigrama(item)
    b = len(big_lista)

    # item a remover
    remA = big_palavra.difference(retorna_bigrama(item))
    remB = big_lista.difference(big_palavra)

    big_lista.update(big_palavra)
    big_lista = remove(remA, remB, big_lista)

    s = (2 * len(big_lista)) / (a + b)
    dict[item] = s
    print(f'palavra: {item}, s:{s}')

print(f'Palavra mais proxima: {max(dict, key=dict.get)}')