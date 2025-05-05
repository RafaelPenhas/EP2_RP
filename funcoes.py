import random

def rolar_dados(numero):

  lista = []

  for i in range(numero):
    lista.append(random.randint(1,6))

  return lista

def guardar_dado (dados_rolados, dados_guardados, guardar):
   novo = []
   guardados = []

   for i in range (len(dados_guardados)):
    guardados.append(dados_guardados[i])
  
   guardados.append(dados_rolados[guardar])
   del dados_rolados[guardar]
   novo = [dados_rolados,guardados]

   return novo

def remover_dado (dados_rolados, dados_guardados, remover):
  rolados = []

  for i in range(len(dados_rolados)):
    rolados.append(dados_rolados[i])

  rolados.append(dados_guardados[remover])
  del dados_guardados[remover]

  novo = [rolados,dados_guardados]
  return novo

def calcula_pontos_regra_simples(lista):

  dicio = {}

  for i in range(len(lista)):
    if lista[i] not in dicio:
      dicio[lista[i]] = 1
    
    else:
      dicio[lista[i]]+= 1

  dicio2 = {}
  lista_num = [1,2,3,4,5,6]

  for num in lista_num:
    if num in dicio.keys():
      for num, qnt in dicio.items():
        dicio2[num] = num*qnt

    else:
      dicio2[num] = 0

  return dicio2

def calcula_pontos_soma(lista):

  soma = 0

  for i in range(len(lista)):
    soma += lista[i]

  return soma

def calcula_pontos_sequencia_baixa(lista):

  if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
    return 15
  
  if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 15
  
  if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 15
  
  else:
    return 0

def calcula_pontos_sequencia_alta(lista):
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 30
  
  if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 30
  
  else:
    return 0
  
def calcula_pontos_full_house(lista):

  dicio = {}
  soma = 0

  for i in range(len(lista)):
    soma += lista[i]
    if lista[i] not in dicio:
      dicio[lista[i]] = 1
  
    else:
      dicio[lista[i]] += 1

  for num, qnt in dicio.items():
    if qnt == 2:
      for num, qnt in dicio.items():
        if qnt == 3:
          return soma
    
    elif qnt == 1 or qnt == 4 or qnt == 5:
      return 0

def calcula_pontos_quadra(lista):

  dicio = {}
  soma = 0
  n = 0

  for i in range(len(lista)):
    soma += lista[i]
    if lista[i] not in dicio:
      dicio[lista[i]] = 1
  
    else:
      dicio[lista[i]] += 1
  
  for num, qnt in dicio.items():
    if qnt >= 4:
      n = 1

  if n == 1:
    return soma

  else:
    return 0    

def calcula_pontos_quina(lista):

  dicio = {}
  soma = 0
  n = 0

  for i in range(len(lista)):
    if lista[i] not in dicio:
      dicio[lista[i]] = 1
  
    else:
      dicio[lista[i]] += 1
  
  for num, qnt in dicio.items():
    if qnt >= 5:
      n = 1

  if n == 1:
    return 50

  else:
    return 0
  
def calcula_pontos_regra_avancada(lista):

  resultado = {
    'cinco_iguais': calcula_pontos_quina(lista),
    'full_house': calcula_pontos_full_house(lista),
    'quadra': calcula_pontos_quadra(lista),
    'sem_combinacao': calcula_pontos_soma(lista),
    'sequencia_alta': calcula_pontos_sequencia_alta(lista),
    'sequencia_baixa': calcula_pontos_sequencia_baixa(lista)
}
  
  return resultado

def faz_jogada(dados, categoria, dicio):

  if categoria == "1":
    categoria = 1
  if categoria == "2":
    categoria = 2
  if categoria == "3":
    categoria = 3
  if categoria == "4":
    categoria = 4
  if categoria == "5":
    categoria = 5
  if categoria == "6":
    categoria = 6

  if categoria in dicio['regra_avancada']:
    dicio['regra_avancada'][categoria] = calcula_pontos_regra_avancada(dados)[categoria]
        
    if categoria in dicio['regra_simples']:
      dicio['regra_simples'][categoria] = calcula_pontos_regra_simples(dados)[categoria]

  return dicio



