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

