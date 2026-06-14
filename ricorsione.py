from random import randint


def Fibonacci(indice):

    if indice <= 1:
        return indice
    else:

        return (Fibonacci(indice-1)+Fibonacci(indice-2))

print(Fibonacci(3))

def fibonacci(indice):
    seq = [0,1]
    for i in range (indice):
       seq.append(seq[-1]+seq[-2])

    return print(seq[:-1])
fibonacci(3)

lista = [1000,6,12,13,89,90,66,118,220,8,899,0,4]

def trova_max(ll):
    """
    :param ll: lista di numeri
    :return: ricorsione delle lista fino
    a trovare il valore più grande.
    Iniziamo con il caso BASE poi si procede con il caso induttivo
    """
    print(ll)
    print(f'La lunghezza della lista è: {len(ll)}')
    if ll[0]>=max(ll):
        return ll[0]
    else:
        return trova_max(ll[1:])
a = trova_max(lista)
print(f'Il valore massimo della lista è: {a} la lista è lunga {len(lista)} elementi')
print()
nome = "Alessandro"
count = 0
for indice,lettera in enumerate (nome):

    if lettera.lower() == 'a':
        ris = indice
        count = count + 1

        print(f'La lettera che cerchi si trova in posizione:{ris}')

def logic_int(x):
    if x>=0.5:
        return 1
    else:
        return 0

def maggioranza(x):
    a = logic_int(x[0])
    b = logic_int(x[1])
    c = logic_int(x[2])
    if a+b+c >= 2:
        return 1
    else:
        return 0

print(maggioranza([0.6,1,0.6]))
print(maggioranza([0.6,0.6,0.5]))
print(maggioranza([0.5,0.5,0.5]))

print(logic_int(0.4))


# for oggetto in lista:
#     print('inizio blocco')
#     print(oggetto)
#     print('fine blocco')
# del lista[0]
# print(lista+[1,2,3,4])
//La torre di hanoi si sviluppta tramite questa tecnologia di programmazione
