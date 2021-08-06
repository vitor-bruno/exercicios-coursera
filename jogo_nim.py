def computador_escolhe_jogada(n, m):
    jogada = 1
    restante = n - jogada
    while (not restante % (m + 1) == 0) and jogada < m and jogada < n:
        jogada += 1
        restante = n - jogada
    return jogada


def usuario_escolhe_jogada(n, m):
    jogada = int(input('Quantas peças você vai tirar? '))
    while not (0 < jogada <= m) or not (0 < jogada <= n):
        print('\nOops! Jogada inválida! Tente de novo.\n')
        jogada = int(input('Quantas peças você vai tirar? '))
    return jogada


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m + 1) == 0:
        print('\nVocê começa!\n')
        while n > 0:
            j = usuario_escolhe_jogada(n, m)
            print('\nVocê tirou', f'{j} peças.' if j > 1 else 'uma peça.')
            n-= j
            if n == 0:
                print('Fim do jogo! Você ganhou!\n')
                return True
            else:
                print('Agora', f'restam {n} peças' if n > 1 else 'resta apenas uma peça','no tabuleiro.\n')
            j = computador_escolhe_jogada(n, m)
            print('O computador tirou', f'{j} peças.' if j > 1 else 'uma peça.')
            n-= j
            if n == 0:
                print('Fim do jogo! O Computador ganhou!\n')
                return False
            else:
                print('Agora', f'restam {n} peças' if n > 1 else 'resta apenas uma peça','no tabuleiro.\n')
    else:
        print('\nComputador começa!\n')
        while n > 0:
            j = computador_escolhe_jogada(n, m)
            print('O computador tirou', f'{j} peças.' if j > 1 else 'uma peça.')
            n-= j
            if n == 0:
                print('Fim do jogo! O Computador ganhou!\n')
                return False
            else:
                print('Agora', f'restam {n} peças' if n > 1 else 'resta apenas uma peça','no tabuleiro.\n')
            j = usuario_escolhe_jogada(n, m)
            print('\nVocê tirou', f'{j} peças.' if j > 1 else 'uma peça.')
            n-= j
            if n == 0:
                print('Fim do jogo! Você ganhou!\n')
                return True
            else:
                print('Agora', f'restam {n} peças' if n > 1 else 'resta apenas uma peça','no tabuleiro.\n')


print('\nBem-vindo ao jogo do NIM! Escolha:\n')
tipo = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n\n'))
if tipo == 1:
    print('\nVocê escolheu uma partida isolada!\n')
    partida()
else:
    print('\nVocê escolheu um campeonato!\n')
    vit_comp = 0
    vit_jog = 0
    for c in range(1, 4):
        print(f'**** Rodada {c} ****\n')
        if not partida():
            vit_comp += 1
        else:
            vit_jog += 1
    print(f'**** Final do campeonato! ****\n\nPlacar: Você {vit_jog} X {vit_comp} Computador')




