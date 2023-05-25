import random

baralho = ['A de Espadas', '2 de Espadas', '3 de Espadas', '4 de Espadas', '5 de Espadas', '6 de Espadas', '7 de Espadas', '8 de Espadas', '9 de Espadas', '10 de Espadas', 'J de Espadas', 'Q de Espadas', 'K de Espadas', 
           'A de Copas', '2 de Copas', '3 de Copas', '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas', '8 de Copas', '9 de Copas', '10 de Copas', 'J de Copas', 'Q de Copas', 'K de Copas',
           'A de Paus', '2 de Paus', '3 de Paus', '4 de Paus', '5 de Paus', '6 de Paus', '7 de Paus', '8 de Paus', '9 de Paus', '10 de Paus', 'J de Paus', 'Q de Paus', 'K de Paus',
           'A de Ouros', '2 de Ouros', '3 de Ouros', '4 de Ouros', '5 de Ouros', '6 de Ouros', '7 de Ouros', '8 de Ouros', '9 de Ouros', '10 de Ouros', 'J de Ouros', 'Q de Ouros', 'K de Ouros']
nome = []
fora = []

def cartas_em_ordem(cartas):
    carta_in_string = ''
    for carta in cartas:
        if carta == cartas[len(cartas)-1]:
            carta_in_string += carta
        else:
            carta_in_string += carta + ', '
    return carta_in_string

def cartas_em_soma(cartas):
    valor_total = 0
    for carta in cartas:
        match carta[0:2]:
            case 'K ' | 'Q ' | 'J ':
                valor_total += 10
            case 'A ':
                valor_total += 1
            case _:
                valor_total += int(carta[0:2])
    return valor_total


def pegarcarta():
    num = random.randrange(len(baralho))
    carta = baralho[num]
    baralho.remove(carta)
    return carta
    
def jogo():
    qtd_players = int(input("Quantas pessoas irão jogar?: ")) #Quantas pessoas irão jogar

    for player in range(qtd_players): #dar as 2 cartas iniciais 
        nome.append({'nome': input(f"Qual o nome do jogador {player+1}?: "),
                                   'cartas': None})
    for n in range(qtd_players):
        nome[n]['cartas'] = [pegarcarta()]
        nome[n]['cartas'] += [pegarcarta()]
        print('nome:',nome[n]['nome'],'| cartas:',cartas_em_ordem(nome[n]['cartas']), '| soma:',cartas_em_soma(nome[n]['cartas']))
    while len(fora) != qtd_players:
        i = 0
        while i < len(nome):
            if cartas_em_soma(nome[i]['cartas']) < 21:
                while True:
                    sORn = input(f"{nome[i]['nome']}, Quer parar? [S] ou [N]: ").upper()
                    if sORn == 'S':
                        fora.append(nome[i])
                        nome.remove(nome[i])
                        if i > 0:
                            i -= 1
                        break
                    elif sORn == 'N':
                        nome[i]['cartas'] += [pegarcarta()]
                        print('nome:',nome[i]['nome'],'| cartas:',cartas_em_ordem(nome[i]['cartas']), '| soma:',cartas_em_soma(nome[i]['cartas']))
                        i += 1
                        break
            else:
                fora.append(nome[i])
                nome.remove(nome[i])
                if i > 0:
                    i -= 1
    ganhador = []  
    for f in range(len(fora)):
        if cartas_em_soma(fora[f]['cartas']) <= 21:
            ganhador += [cartas_em_soma(fora[f]['cartas'])]
    for g in range(len(fora)):
        if cartas_em_soma(fora[g]['cartas']) == max(ganhador):
            print('O ganhador é: {} com {} pontos'.format(fora[g]['nome'],cartas_em_soma(fora[g]['cartas'])))

jogo()