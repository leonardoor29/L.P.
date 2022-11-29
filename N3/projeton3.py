A = ['A1','A2','A3','A4','A5','A6','A7']
B = ['B1','B2','B3','B4','B5','B6','B7']
C = ['C1','C2','C3','C4','C5','C6','C7']
rodada = 0
while rodada < 3:
    print("A  B  C")
    for i in range(0,7):
        print(A[i],B[i],C[i])
    escolha = input("Escolha uma das colunas: ")
    print("############################################")
    if escolha == 'A' or escolha == 'a':
        juntar = B+A+C
    elif escolha == 'B' or escolha == 'b':
        juntar = A+B+C
    else:
        juntar = A+C+B
    n = 3
    juntar = [juntar[i::n] for i in range(3)]
    A = juntar[0]
    B = juntar[1]
    C = juntar[2]
    rodada += 1
resultado = A+B+C
print("O resultado é: ", resultado[10])