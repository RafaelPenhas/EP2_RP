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


