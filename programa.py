import funcoes

# print(funcoes.imprime_cartela([5, 3, 3, 3, 3]))

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

funcoes.imprime_cartela(cartela) 
a = [0,1,2,3,4,5,6,7,8,9,10,11,12]
dados_rolados = funcoes.rolar_dados(5)
print(f'Dados rolados: {dados_rolados}')

dados_guardados = []
print(f'Dados guardados: {dados_guardados}')

opcoes_validas = [0,1,2,3,4]
# print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ')
# opcao = int(input())

lista_jogadas_cartela = [1,2,3,4,5,6,'sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

for i in range(len(lista_jogadas_cartela)):
    # while cartela['regra_simples'][i] == -1 or cartela['regra_avancada'][i] == -1:
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ')
    opcao = int(input())
    if opcao == 1:
        print('Digite o índice do dado a ser guardado (0 a 4):')
        guardar = int(input())
        dados_rolados = funcoes.guardar_dado(dados_rolados, dados_guardados, guardar)[0]
        print(f'Dados rolados: {dados_rolados}')
        dados_guardados = funcoes.guardar_dado(dados_rolados, dados_guardados, guardar)[1]
        print(f'Dados guardados: {dados_guardados}')

    if opcao == 2:
        print('Digite o índice do dado a ser removido (0 a 4): ')
        qual_remover = int(input())
        remover = funcoes.remover_dado(dados_rolados, dados_guardados, qual_remover)
        dados_rolados = remover[:,0]
        dados_guardados = remover[:,1]
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')

    if opcao == 3:
        b = 1
        if b <= 2:
            dados_rolados = funcoes.rolar_dados(len(dados_rolados))
            print(f'Dados rolados: {dados_rolados}')
            print(f'Dados guardados: {dados_guardados}')
            b += 1
        
        else:
            print('Você já usou todas as rerrolagens.')

    if opcao == 4:
        cartela = funcoes.imprime_cartela(cartela)
        print(f'Cartela de Pontos: {cartela}')

    if opcao == 0:
        print('Digite a combinação desejada: ')
        combinacao = input()

        b = 1 
        while b != 0:
            if combinacao not in cartela:
                print('Combinação inválida. Tente novamente.')
                combinacao = input()
            
            else:
                b = 0

        b = 1
        while b != 0:
            if cartela[combinacao] > 0:
                print('Essa combinação já foi utilizada.')
                combinacao = input()
            
            else:
                b = 0

        funcoes.faz_jogada(dados_rolados, combinacao, cartela)
        dados_rolados = funcoes.rolar_dados(5)
        print(f'Dados rolados: {dados_rolados}')
        dados_guardados = funcoes.guardar_dados(dados_rolados, dados_guardados, guardar)[:,1]
        print(f'Dados guardados: {dados_guardados}')

    b = 1
    while b != 0:
        if opcao not in opcoes_validas:
            print('Opção inválida. Tente novamente.')
            opcao = input()
        
        else:
            b = 0

soma = 0
for jogada, pontos in cartela.items():
    soma += pontos

print(f'Pontuação total: {soma}')