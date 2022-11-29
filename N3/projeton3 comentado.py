A = ['A1','A2','A3','A4','A5','A6','A7'] #O Array "A" onde comporta o primeiro conjunto de cartas
B = ['B1','B2','B3','B4','B5','B6','B7'] #O Array "B" onde comporta o segundo conjunto de cartas
C = ['C1','C2','C3','C4','C5','C6','C7'] #O Array "C" onde comporta o terceiro conjunto de cartas

#a cima mostra as 3 listas de cartas usadas na mágica
rodada = 0 # Em qual rodada o sistema está
while rodada < 3: #usamos o "While" para repetir o embaralhamento a quantidade de rodadas
    print("A  B  C") #Aqui printamos um texto simples para organizar melhor
    for i in range(0,7): #Aqui o "for" repete "i" com a quantidade definida de vezes "7"
        print(A[i],B[i],C[i]) # Nesta linha printa as Array ao usuario
    escolha = input("Escolha uma das colunas: ") # Nesta linha é onde o usuario informa qual o conjunto escolhido
    print("############################################") #Um print simples para organizar a tela ao cliente
    if escolha == 'A' or escolha == 'a': #Abrimos o "if" para definir o que o sistema vai fazer dependendo da escolha do usuario
        juntar = B+A+C
    elif escolha == 'B' or escolha == 'b':
        juntar = A+B+C
    else:
        juntar = A+C+B
    n = 3 #Aqui onde embaralham as cartas e apresentam a baixo as novas array
    juntar = [juntar[i::n] for i in range(3)]
    A = juntar[0]
    B = juntar[1]
    C = juntar[2]
    rodada += 1 #Como a rodada começa com 0 a cada execução soma mais 1 até o limite de 3 repetições
resultado = A+B+C # "resultado" traz a junção das array e após as "3" embaralhadas e faz a junção para mostrar o resultado
print("O resultado é: ", resultado[10]) #Aqui mostra o resultado ao usuario