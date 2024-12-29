rows = 9
for i in range(0, rows + 1):
    # Adiciona espaços no início de cada linha para inverter a direção
    for space in range(i):
        print(" ", end=" ")
    # Imprime os números em ordem decrescente
    for j in range(rows - i, 0, -1):
        print(j, end=" ")
    print()
input()
