matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas}, {colunas}]: '))
print('-=' * 20)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print()
