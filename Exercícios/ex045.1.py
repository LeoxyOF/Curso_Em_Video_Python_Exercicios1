while True:
    import random
    from time import sleep
    print('\033[1;31m=========={ \033[1;33mPedra, \033[1;32mPapel e \033[1;35m', end='')
    print('Tesoura\033[m\033[1;31m }==========\033[m\n')
    pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
    print('\033[1;31m✯Pedra\n\033[1;35m     ✯Papel\033[1;33m\n         ✯Tesoura\033[m\n')
    resp = str(input('\033[1;36mQual sua escolha? ')).strip().capitalize()
    print('')
# Pedra
    if pc == 'Pedra' and resp == 'Pedra':
        print('\033[1;31mPedra \033[m')

        sleep(1)
        print('\033[1;36m    VS\033[m')
        sleep(1)
        print('\033[1;32m       Pedra')
        sleep(1)
        print('\n\033[1;33m♦\033[1;34m Empate!')
    elif pc == 'Tesoura' and resp == 'Pedra':
        print('\033[1;31mPedra \033[m')
        sleep(1)
        print('\033[1;36m     VS\033[m')
        sleep(1)
        print('\033[1;32m       Tesoura')
        sleep(1)
        print('\n\033[1;33m♛\033[1;32m Você Venceu! :)')
    elif pc == 'Papel' and resp == 'Pedra':
        print('\033[1;31mPedra \033[m')
        sleep(1)
        print('\033[1;36m     VS\033[m')
        sleep(1)
        print('\033[1;32m       Papel')
        sleep(1)
        print('\n\033[1;31m Você Perdeu! :(')
# Papel
    elif pc == 'Papel' and resp == 'Papel':
        print('\033[1;31mPapel \033[m')
        sleep(1)
        print('\033[1;36m    VS\033[m')
        sleep(1)
        print('\033[1;32m       Papel')
        sleep(1)
        print('\n\033[1;33m♦\033[1;34m Empate!')
    elif pc == 'Pedra' and resp == 'Papel':
        print('\033[1;31mPapel \033[m')
        sleep(1)
        print('\033[1;36m     VS\033[m')
        sleep(1)
        print('\033[1;32m       Pedra')
        sleep(1)
        print('\n\033[1;33m♛\033[1;32m Você Venceu! :)')
    elif pc == 'Tesoura' and resp == 'Papel':
        print('\033[1;31mPapel \033[m')
        sleep(1)
        print('\033[1;36m     VS\033[m')
        sleep(1)
        print('\033[1;32m       Tesoura')
        sleep(1)
        print('\n\033[1;31m Você Perdeu! :(')
    # Tesoura
    elif pc == 'Tesoura' and resp == 'Tesoura':
        print('\033[1;31mTesoura \033[m')
        sleep(1)
        print('\033[1;36m       VS\033[m')
        sleep(1)
        print('\033[1;32m          Tesoura')
        sleep(1)
        print('\n\033[1;33m♦\033[1;34m Empate!')
    elif pc == 'Papel' and resp == 'Tesoura':
        print('\033[1;31mTesoura \033[m')
        sleep(1)
        print('\033[1;36m       VS\033[m')
        sleep(1)
        print('\033[1;32m          Papel')
        sleep(1)
        print('\n\033[1;33m♛\033[1;32m Você Venceu! :)')
    elif pc == 'Pedra' and resp == 'Tesoura':
        print('\033[1;31mTesoura \033[m')
        sleep(1)
        print('\033[1;36m       VS\033[m')
        sleep(1)
        print('\033[1;32m          Pedra')
        sleep(1)
        print('\n\033[1;31m Você Perdeu! :(')
    sleep(2)
    print('\n')
