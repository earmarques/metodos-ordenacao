#!/usr/bin/env python3
#coding=utf-8

 #####################################################
#                                                    #
#  author: Éder A. R. Marques                        #
#  email:  earmarques@gmail.com                      #
#  local:  São José do Rio Preto/SP Brazil           #
#  date:   28/10/2020                                #
#                                                    #
#  versioned for Python 2 from the Professor's       #
#  original C code.                                  #
#  ------------------------------------------------  #
#  professor: Carlos Magnus Carlson Filho            #
#  course:    Estruturas de Dados                    #
#  program:   Análise e Desenvolvimento de Sistemas  #
#  college:   Fatec Rio Preto                        #
#                                                    #
####################################################


import random
from datetime import datetime


# ==================================================================================================
# Cabeçalho     ------------------------------------------------------------------------------------

print("\n\n")
print("\033[1;{:_^80}".format("  Métodos de Ordenação  "))
print("\033[0;")


# ==================================================================================================
# Constantes     -----------------------------------------------------------------------------------

# Constantes para escolha do método de ordenação
BOLHA_DIRETO =              1
BOLHA_INVERTIDO =           2
INSERCAO =                  3
SELECAO  =                  4
MESCLAGEM_NAO_RECURSIVO =   5
MESCLAGEM_RECURSIVO =       6
QUICK_RECURSIVO =           7
QUICK_RECURSIVO_CAUDAL_1 = 71
QUICK_RECURSIVO_CAUDAL_2 = 72
MUDAR_METODO =              8
SAIR =                      9

# Constantes para escolha do tipo de teste do método de ordenção
FIXO =                 1
GRANDE_1_ALEATORIO =   2
GRANDE_2_ALEATORIO =   3
GRANDE_1_DECRESCENTE = 4
GRANDE_2_DECRESCENTE = 5


# ==================================================================================================
# Menus de Interação com o Usuário     -------------------------------------------------------------

# Menu 1 - Método de Ordenação     -----------------------------------------------------------------

def escolhe_metodo():

  """ Retorna o método escolhido para o teste.

  Apresenta uma menu de opções para que o usuário escolha o método de ordenação.

  Opções:
      1  - Bolha direto    (bubble sort)    - esquerda->direita
      2  - Bolha invertido (bubble sort)    - direita->esquerda
      3  - Inserção     (insertion sort)
      4  - Seleção      (selection sort)
      5  - Mesclagem    (merge sort)        - não recursivo
      6  - Mesclagem    (merge sort)        - recursivo
      7  - Partição     (quick sort)        - recursivo
      71 - Partição     (quick sort tail 1) - recursivo
      72 - Partição     (quick sort tail 2) - recursivo
      9  - Sair do programa

  Returns:
      int: A escolha do usuário.
  """

  escolha = None

  # Exibição das opções
  print('_{:-<47}'.format(''))
  print('{}'.format('Escolha do método de ordenação a ser executado:'))
  print('{:-<47}'.format(''))
  print('  1 - Bolha direto    (bubble sort)    - esquerda->direita')
  print('  2 - Bolha invertido (bubble sort)    - direita->esquerda')
  print('  3 - Inserção     (insertion sort)')
  print('  4 - Seleção      (selection sort)')
  print('  5 - Mesclagem    (merge sort)        - não recursivo')
  print('  6 - Mesclagem    (merge sort)        - recursivo')
  print('  7 - Partição     (quick sort)        - recursivo')
  print(' 71 - Partição     (quick sort tail 1) - recursivo')
  print(' 72 - Partição     (quick sort tail 2) - recursivo')
  print('  9 - Sair do programa')

  # Obtenção, via teclado, da escolha do usuário
  escolha = int(input('\nInforme a opção desejada: '))

  return escolha


# Menu 2 - Tipo de Teste de Carga - Benchmark     --------------------------------------------------

def escolhe_teste():

  """ Retorna o tipo de teste escolhido.

  Apresenta uma menu de opções para que o usuário escolha do tipo de teste de carga
  para fazer análise de desempenho do método de ordenação escolhido.

  Opões:
      1 - Vetor fixo para validação do método de ordenação
      2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente
      3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente
      4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes
      5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes
      8 - Voltar à escolha do método de ordenação
      9 - Sair do programa

  Returns:
      int: A escolha do usuário.
  """
  escolha = None;

  # Exibição das opções
  print('\n{:-<41}'.format(''))
  print('{}'.format('Escolha do tipo de teste a ser executado:'))
  print('{:-<41}'.format(''))

  print(' 1 - Vetor fixo para validação do método de ordenação')
  print(' 2 - Vetor grande 1 (20000 elementos) preenchido aleatoriamente')
  print(' 3 - Vetor grande 2 (40000 elementos) preenchido aleatoriamente')
  print(' 4 - Vetor grande 1 (20000 elementos) preenchido com valores decrescentes')
  print(' 5 - Vetor grande 2 (40000 elementos) preenchido com valores decrescentes')
  print(' 8 - Voltar à escolha do método de ordenação')
  print(' 9 - Sair do programa')

  # Obtenção, via teclado, da escolha do usuário
  escolha = int(input('\nInforme a opção desejada:'))

  return escolha


# ==================================================================================================
# Montagem dos Vetores de Testes     ---------------------------------------------------------------

# Vetor de Validação - 8 Elementos Aleatórios     --------------------------------------------------

def monta_vetor_FIXO(metodo_ordenacao):

  """ Procedimento que monta o VETOR FIXO e o imprime antes da ordenação.

  Args:
      metodo_ordenacao (str): O nome do método.

  Returns:
    list: Um vetor pequeno para validação dos métodos.
  """

  print('\n------------------------------------')
  print('Inicializando dados do vetor V1 para: {}'.format(metodo_ordenacao))
  print('------------------------------------')

  V1 = [89, 44, 75, 66, 11, 38, 93, 56]

  #V1 = [3,0,1,8,7,2,5,4,9,6]  # vetor da dança húngara: https://www.youtube.com/watch?v=ywWBy6J5gz8

  print('Valor de V1: {}'.format(V1))

  return V1


# 20.000 Elementos - Ordem Decrescente     ---------------------------------------------------------

def monta_vetor_GRANDE_1_DECRESCENTE(metodo_ordenacao):

  """ Procedimento que monta o VETOR GRANDE 1 e o preenche com números decrescentes.

  Args:
      metodo_ordenacao (str): O nome do método.

  Returns:
    list: Um vetor de 20.000 elementos em ordem descrescente.
  """

  print('\n------------------------------------')
  print('Inicializando dados do vetor T1 para: {}'.format(metodo_ordenacao))
  print('------------------------------------')

  T1=[]
  for i in range(20000):
    T1.append(20000 - i)

  print('\nVocê escolheu gerar vetores com números decrescentes !')
  print('Primeiro elemento de T1: {}'.format( T1[0] ))
  print('Último   elemento de T1: {}'.format( T1[19999] ))

  return T1


# 40.000 Elementos - Ordem Decrescente     ---------------------------------------------------------

def monta_vetor_GRANDE_2_DECRESCENTE(metodo_ordenacao):

  """ Procedimento que monta o VETOR GRANDE 2 e o preenche com números decrescentes.

  Args:
      metodo_ordenacao (str): O nome do método.

  Returns:
    list: Um vetor de 40.000 elementos em ordem descrescente.
  """
  print('\n------------------------------------')
  print('Inicializando dados do vetor T2 para: {}'.format(metodo_ordenacao))
  print('------------------------------------')

  T2=[]
  for i in range(40000):
    T2.append(40000 - i)

  print('\nVocê escolheu gerar vetores com números decrescentes !')
  print('Primeiro elemento de T2: {}'.format( T2[0] ))
  print('Último   elemento de T2: {}'.format( T2[39999] ))

  return T2


# 20.000 Elementos - Aleatórios     ----------------------------------------------------------------

def monta_vetor_GRANDE_1_ALEATORIO(metodo_ordenacao):

  """ Procedimento que monta o VETOR GRANDE 1 e o preenche com números aleatórios.

  Args:
      metodo_ordenacao (str): O nome do método.

  Returns:
    list: Um vetor de 20.000 elementos aleatórios.
  """
  print('\n------------------------------------')
  print('Inicializando dados do vetor T1 para: {}'.format(metodo_ordenacao))
  print('------------------------------------')

  T1=[]
  for i in range(20000):
    T1.append( random.randint(1, 20000) )

  print('\nVocê escolheu gerar vetores com números aleatórios !')
  print('Primeiro elemento de T1: {}'.format( T1[0] ))
  print('Último   elemento de T1: {}'.format( T1[19999] ))

  return T1


# 40.000 Elementos - Aleatórios     ----------------------------------------------------------------

def monta_vetor_GRANDE_2_ALEATORIO(metodo_ordenacao):

  """ Procedimento que monta o VETOR GRANDE 2 e o preenche com números aleatórios.

  Args:
      metodo_ordenacao (str): O nome do método.

  Returns:
    list: Um vetor de 40.000 elementos aleatórios.
  """
  print('\n------------------------------------')
  print('Inicializando dados do vetor T2 para: {}'.format(metodo_ordenacao))
  print('------------------------------------')

  T2=[]
  for i in range(40000):
    T2.append( random.randint(1, 40000) )

  print('\nVocê escolheu gerar vetores com números aleatórios !')
  print('Primeiro elemento de T2: {}'.format( T2[0] ))
  print('Último   elemento de T2: {}'.format( T2[39999] ))

  return T2


# ==================================================================================================
# Métodos de Ordenação     -------------------------------------------------------------------------

# Bubble Sort     ----------------------------------------------------------------------------------

def bubble_sort(vetor, imprimir=False):

  """ Método da BOLHA - Bubble Sort - Percurso Esquerda -> Direita.

  Args:
      vetor (list): Vetor a ser ordenado.
      n (int): Tamanho da porção do vetor que ainda não está ordenada.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: O vetor fornecido como parâmetro ordenado.
  """
  # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
  trocou = True        # inicia com true só para entrar no loop
  n = len(vetor)       # número de elementos no vetor
  cursor = n           # posição do cursor, inicialmente após o último elemento

  # loop de passos
  while trocou:
    # reinicializa porque se supõe que neste passo ainda não houve troca
    trocou = False
    # recua o cursor em uma posição
    cursor -= 1

    if imprimir: print('Passo {}'.format(n - cursor))

    # loop de trocas dentro do passo, até o cursor
    for i in range(cursor):

      if vetor[i] > vetor[i + 1]:

        # troca a posição dos dois elementos adjacentes
        temp = vetor[i]
        vetor[i] = vetor[i + 1]
        vetor[i + 1] = temp
        trocou = True

    if imprimir: print('Valor de V1: {}'.format(vetor))

  # retorna vetor ordenado
  return vetor


# Bubble Sort Invertido     ------------------------------------------------------------------------

def bubble_sort_invertido(vetor, imprimir=False):

  """ Método da BOLHA - Bubble Sort - Percurso Direita -> Esquerda.

  Args:
      vetor (list): Vetor a ser ordenado.
      n (int): Tamanho da porção do vetor que ainda não está ordenada.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: O vetor fornecido como parâmetro ordenado.
  """
  # Auxiliar para interromper o loop - se não houver troca de posição o vetor está ordenado
  trocou = True       # inicia com true só para entrar no loop
  n = len(vetor)      # número de elementos no vetor
  cursor = -1          # posição do cursor, inicialmente antes do primeiro elemento

  # loop de passos
  while trocou:
   # reinicializa porque se supõe que neste passo ainda não houve troca
   trocou = False
   # avança o cursor em uma posição
   cursor += 1

   if imprimir: print('Passo {}'.format(cursor + 1))

   # loop de trocas dentro do passo, até o cursor
   for i in range(n - 1, cursor, -1):

     if vetor[i] < vetor[i - 1]:

       # troca a posição dos dois elementos adjacentes
       temp = vetor[i]
       vetor[i] = vetor[i - 1]
       vetor[i - 1] = temp
       trocou = True

   if imprimir: print('Valor de V1: {}'.format(vetor))

  # retorna vetor ordenado
  return vetor


# Insertion Sort     -----------------------------------------------------------------------------

def insertion_sort(vetor, imprimir=False):

  """ Método da INSERÇÃO - Insertion Sort.

  Args:
      vetor (list): Vetor a ser ordenado.
      n (int): Tamanho da porção do vetor que ainda não está ordenada.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: O vetor fornecido como parâmetro ordenado.
  """

  n = len(vetor)      # número de elementos no vetor
  cursor = 0           # posição do cursor, inicialmente no primeiro elemento

  # loop de passos
  for passo in range(1, n):

   if imprimir: print('Passo {}'.format(passo))

   # avança o cursor em uma posição
   cursor += 1;

   # Corro todos os elementos do fim para trás até a posição do cursor,
   # se o vetor[cursor] for menor que o antecessor, troco de posição e
   # comparo com anterior seguinte, levando o elemento (se menor) até a sua posição correta
   for i in range(cursor, 0, -1):
     # do cursor pra trás, todos os elementos já estão em ordem crescente,
     # se o elemento for maior que seu antecessor ele já está na posição correta,
     # posso interromper o loop e ir ao próximo elemento
     if vetor[i - 1] < vetor[i]:
       break

     # troca a posição dos dois elementos adjacentes
     temp = vetor[i]
     vetor[i] = vetor[i - 1]
     vetor[i - 1] = temp

   if imprimir: print('Valor de V1: {}'.format(vetor))

  # retorna vetor ordenado
  return vetor


# Selection Sort     -------------------------------------------------------------------------------

def selection_sort(vetor, imprimir=False):

  """ Método da SELEÇÃO - Selection Sort.

  Args:
      vetor (list): Vetor a ser ordenado.
      n (int): Tamanho da porção do vetor que ainda não está ordenada.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: O vetor fornecido como parâmetro ordenado.
  """
  # Variáveis auxiliares
  indice_menor = -1
  n = len(vetor)      # número de elementos no vetor
  cursor = -1          # posição do cursor, inicialmente antes do primeiro elemento


  # loop de passos
  for passo in range(1, n):

    if imprimir: print('Passo {}'.format(passo))

    # avança o cursor em uma posição
    cursor += 1;
    # encontra o menor valor dentre os elementos não ordenados
    menor = vetor[cursor]
    indice_menor = cursor
    for i in range(cursor + 1, n):
      if vetor[i] < menor:
        menor = vetor[i]
        indice_menor = i

    # troca o menor com o elemento ao lado direito do cursor
    vetor[indice_menor] = vetor[cursor]
    vetor[cursor] = menor

    if imprimir: print('Valor de V1: {}'.format(vetor))

  # retorna vetor ordenado
  return vetor


# Merge Sort    ------------------------------------------------------------------------------------

def merge_sort(metade_esquerda, metade_direita, imprimir=False):

  """ Método da MESCLAGEM - Merge Sort.

  Por não ser o recursivo e ordena as duas metades primeiramente para depois mesclar
  os elementos em ordem crescente.

  Args:
      metade_esquerda (list): primeira metade
      metade_direita (list): segunda metade
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: Um vetor ordenado.
  """
  i = j = passo = 0
  tamanho_metade_esquerda = len(metade_esquerda)
  tamanho_metade_direita  = len(metade_direita)

  # Para garantir que as duas metades estejam ordenadas, passamos os vetores pelo Bubble Sort.
  # Se estiverem previamente ordenadas, o método bubble sort vai descobrir em apenas uma
  # passada pelo vetor e retornará rapidamente.
  metade_esquerda = bubble_sort(metade_esquerda, imprimir)
  metade_direita  = bubble_sort(metade_direita,  imprimir)

  # Cria o vetor que receberá os elementos ordenados
  vetor = list(metade_esquerda)
  vetor.extend(metade_direita)


  # Compara as duas metades sequencialmentes e adiciona no vetor de forma crescente.
  # OBS IMPORTANTE|=> as duas metades precisam já estarem ordenadas

  while passo < (tamanho_metade_esquerda + tamanho_metade_direita):

    if imprimir: print('Passo {}'.format(passo + 1))

    # Comparo os elementos de ambos os lados
    if metade_esquerda[i] <= metade_direita[j]:
      # guardo o de menor valor que está do lado esquerdo
      vetor[passo] = metade_esquerda[i]
      # ando pra frente no vetor do lado esquerdo
      i += 1
      # se já terminei de fazer comparações com a primeira metade, do lado esquerdo
      if i == tamanho_metade_esquerda:
        # copio o resto dos elementos da segunda metade do lado direito
        while j < tamanho_metade_direita:
          passo += 1
          vetor[passo] = metade_direita[j]
          j += 1
    else:
      # guardo o de menor valor que está do lado direito
      vetor[passo] = metade_direita[j]
      # ando pra frente no vetor do lado direito
      j += 1
      # se já terminei a segunda metade, do lado direito
      if j == tamanho_metade_direita:
        # copio os elementos restantes da metade esquerda
        while i < tamanho_metade_esquerda:
          passo += 1
          vetor[passo] = metade_esquerda[i]
          i += 1

    passo += 1

    if imprimir: print('Valor de V1: {}'.format(vetor))

  # retorna vetor ordenado
  return vetor


# Merge Sort - Serviço Completo     ----------------------------------------------------------------

def merge_sort_full_service(vetor, imprimir=False):

  """ Método da MESCLAGEM - Merge Sort.

  Divide o vetor em duas metades e invoca o #merge_sort() para fazer efetivamente a ordenação.

  Args:
      vetor (list): Vetor que será ordenado.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: Um novo vetor ordenado.
  """
  tamanho = len(vetor)
  meio = int(tamanho / 2)
  metade_esquerda = vetor[:meio]
  metade_direita  = vetor[meio:tamanho]

  if imprimir:
    print('metade_esquerda: {}'.format(metade_esquerda))
    print('metade_direita:  {}'.format(metade_direita))

  # retorna um novo vetor ordenado
  return merge_sort(metade_esquerda, metade_direita, imprimir)


# Merge Sort Recursivo     -------------------------------------------------------------------------

def merge_sort_recursivo(vetor, imprimir=False):

  """ Método da MESCLAGEM - Merge Sort - Versão Recursiva.

  Divide o vetor em duas metades e invoca o merge_sort recursivamente para fazer efetivamente a ordenação.

  Args:
      vetor (list): Vetor que será ordenado.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    list: O vetor ordenado.
  """

  if imprimir: print('ENTRADA - Elementos do vetor: {}'.format(vetor))

  tamanho = len(vetor)

  # CASO BASE: tamanho == 1 (nada a fazer)
  if tamanho == 1:
    return vetor

  # RECURSÃO

  meio = int(tamanho / 2)
  metade_esquerda = vetor[:meio]
  metade_direita  = vetor[meio:tamanho]

  tamanho_metade_esquerda = len(metade_esquerda)
  tamanho_metade_direita = len(metade_direita)


  if imprimir:
    print('ENTRADA - Elementos da metade esquerda: {}'.format(metade_esquerda))
    print('ENTRADA - Elementos da metade direita:  {}\n'.format(metade_direita))


  # Recursividade - Aciona a ordenação recursiva para cada metade

  metade_esquerda = merge_sort_recursivo(metade_esquerda, imprimir)
  metade_direita = merge_sort_recursivo(metade_direita, imprimir)


  # Mescla as metades, reconstruindo o vetor ordenadamente

  i = j = passo = 0

  while passo < tamanho:

    if imprimir: print('Passo {}'.format(passo + 1))

    # Comparo os elementos de ambos os lados
    if metade_esquerda[i] <= metade_direita[j]:
      # guardo o de menor valor que está do lado esquerdo
      vetor[passo] = metade_esquerda[i]
      # ando pra frente no vetor do lado esquerdo
      i += 1
      # se já terminei de fazer comparações com a primeira metade do lado esquerdo
      if i == tamanho_metade_esquerda:
        # copio o resto dos elementos da segunda metade do lado direito que já estão ordenados
        while j < tamanho_metade_direita:
          passo += 1
          vetor[passo] = metade_direita[j]
          j += 1
    else:
      # guardo o de menor valor que está do lado direito
      vetor[passo] = metade_direita[j]
      # ando pra frente no vetor do lado direito
      j += 1
      # Se já terminei a segunda metade, é porque já copie todos os elementos do lado direito
      # para o vetor final ordenado e todos os demais restantes do lado esquerdo são valores maiores.
      # Não há mais nenhum elemento do lado direito que seja menor que do lado esquerdo.
      if j == tamanho_metade_direita:
        # copio os elementos restantes da metade esquerda
        while i < tamanho_metade_esquerda:
          passo += 1
          vetor[passo] = metade_esquerda[i]
          i += 1

    passo += 1

  if imprimir: print('\nSAÍDA - Elementos do vetor: {}\n'.format(vetor))

  # retorna o vetor ordenado
  return vetor


# Particionador do Quick Sort     ------------------------------------------------------------------

def particionar(vetor, indice_inicial, indice_final, imprimir=False):

  """ Particionador do Quick Sort

  Pega o elemento(pivô) do vetor cujo indice ou posição é dado por 'indice_inicial', ``vetor[indice_inicial]``,
  e encontra a posição correta do elemento e retorna o índice referente a posição correta.
  Chamaremos este elemento que estamos procurando sua posição simplesmente de 'elemento_pivo_investigado'.

  O algoritmo usa dois cursores para correr o vetor no intevalo dos índices [inicial ao final(inclusive)].
  O cursor da extremidade esquerda avança para a direita até encontrar o elemento subsequente que seja
  maior que o elemento_pivo_investigado. O cursor da direita recua para a esquerda até encontrar
  um elemento que seja menor que o elemento_pivo_investigado. Nessa situação, teremos:

      elemento_esquerda > elemento_pivo_investigado > elemento_direita, logo,
      elemento_esquerda > elemento_direita

  Isto é, está fora de ordem, e o algoritmo já os troca de posição ordenando-os, depois prossegue
  em direção ao centro até que os cursores volantes se encontrarem.

  A condição de parada ocorre quando o cursor da esquerda atropela o da direita, ficando com um valor maior.
  O cursor da direita estará com o índice da posição correta, sendo ele o valor retornado pela função.

  Sinteticamente expresso de uma maneira formal matemática seria:

      Recebe vetor v[p..r] com p < r. Rearranja os elementos do vetor e
      devolve j em p..r tal que v[p..j-1] <= v[j] < v[j+1..r].

  Args:
      vetor (list): Vetor que será ordenado e particionado logicamente.
      indice_inical(int): Índice inicial do intervalo de pesquisa e que determina o elemento pivô cuja posição
      correta será retornada como a posição do pivô do particionamento.
      indice_final(int): Índice final do intervalo de pesquisa.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    int: A posição do pivô do particionamento do vetor.
  """
  elemento_pivo = vetor[indice_inicial]    # ..a ser investigado qual o seu posicionamento correto no vetor
  cursor_esquerda = indice_inicial         # posicionado no primeiro elemento
  cursor_direita = indice_final            # posicionado no último elemento
  posicao_correta_pivo = -1

  # A missão primária é encontrar a #posicao_correta_pivo dentro do vetor, mas durante o processo
  # já vai ordenando, trocando de posição alguns elementos; os que são menores que o pivô e estejam
  # a direita são trocados com elementos que são maiores que o pivô, mas que estão do lado esquerdo.

  while cursor_esquerda <= cursor_direita:

    # Encontra o elemento subsequente que seja maior que o elemento pivô investigado
    if vetor[cursor_esquerda] <= elemento_pivo:
      cursor_esquerda += 1          # avança

    # Encontra, do fim para o começo, o elemento que seja menor que o elemento pivô investigado
    elif vetor[cursor_direita] > elemento_pivo:
      cursor_direita -= 1           # recua

    # |=> vetor[cursor_esquerda] >= elemento_pivo > vetor[cursor_direita] =>
    # logo, vetor[cursor_esquerda] > vetor[cursor_direita], isto é, está fora da ordem crescente,
    # o menor tem de ficar a esquerda e o maior a direita, vamos trocá-los de posição
    else:
      temp = vetor[cursor_esquerda]
      vetor[cursor_esquerda] = vetor[cursor_direita]
      vetor[cursor_direita] = temp
      # A posição correta do elemento pivô investigado está entre os cursores; continuando a procura
      cursor_esquerda += 1     # avança uma posição
      cursor_direita  -= 1     # recua  uma posição

  # A posição correta do elemento pivô é dado pelo cursor_direita
  posicao_correta_pivo = cursor_direita

  # Vamos trocar de posição, fazendo backup do elemento que está ocupando o lugar
  # do nosso elemento pivô investigado para o lugar do pivô (início do vetor)
  vetor[indice_inicial] = vetor[posicao_correta_pivo]
  vetor[posicao_correta_pivo] = elemento_pivo       # copia o elemento pivô para sua posição correta

  if imprimir: print('\nValor de V1: {}'.format(vetor))


  return posicao_correta_pivo


# Quick Sort Recursivo     -------------------------------------------------------------------------

def quick_sort(vetor, indice_inicial, indice_final, imprimir=False):

  """ Quick Sort - Recursão comum.

  Recebe um vetor vetor[indice_inicial..indice_final], com indice_inicial <= indice_final + 1,
  e rearranja o vetor em ordem crescente.

  Args:
      vetor (list): Vetor que será ordenado.
      indice_inicial(int): Índice inicial do intervalo de pesquisa.
      indice_final(int): Índice final do intervalo de pesquisa.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    None: Nada retorna. Opera diretamente com a referência do vetor.
  """
  posicao_pivo_particao = -1

  if indice_inicial < indice_final:    # indices
    posicao_pivo_particao = particionar(vetor, indice_inicial, indice_final, imprimir)

    # partição esquerda
    quick_sort(vetor, indice_inicial, posicao_pivo_particao - 1, imprimir)
    # partição direita
    quick_sort(vetor, posicao_pivo_particao + 1, indice_final, imprimir)


# Quick Sort Recursivo Caudal - Versão 1     -------------------------------------------------------

def quick_sort_tail_1(vetor, indice_inicial, indice_final, imprimir=False):

  """ Quick Sort Recursivo Caudal - Versão 1

  A recursividade ocorre em uma partição de cada vez.

  Args:
      vetor (list): Vetor que será ordenado.
      indice_inicial(int): Índice inicial do intervalo de pesquisa.
      indice_final(int): Índice final do intervalo de pesquisa.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    None: Nada retorna. Opera diretamente com a referência do vetor.
  """

  posicao_pivo_particao = -1

  while indice_inicial < indice_final:

    posicao_pivo_particao = particionar(vetor, indice_inicial, indice_final, imprimir)

    # Ordena SEPARADAMENTE elementos 'antes' e 'depois' da partição
    quick_sort_tail_1(vetor, indice_inicial, posicao_pivo_particao - 1, imprimir)

    indice_inicial = posicao_pivo_particao + 1


# Quick Sort Recursivo Caudal - Versão 2     -------------------------------------------------------

def quick_sort_tail_2(vetor, indice_inicial, indice_final, imprimir=False):

  """ Quick Sort Recursivo Caudal - Versão 2

  Melhor otimização em relação a memória, pois a recursividade ocorre em apenas uma partição, e esta
  partição é a menor, fazendo com que a profundidade das chamadas recursivas seja mais rasa.

  Requer espaço auxiliar O(Log n) no pior caso.

  Args:
      vetor (list): Vetor que será ordenado.
      indice_inicial(int): Índice inicial do intervalo de pesquisa.
      indice_final(int): Índice final do intervalo de pesquisa.
      imprimir (bool, optional): Chave para imprimir ou não os passos intermediários.
      Defaults to False.

  Returns:
    None: Nada retorna. Opera diretamente com a referência do vetor.


  .. _See below link for complete running code:
      https://ide.geeksforgeeks.org/qrlM31
  """
  posicao_pivo_particao = -1

  while indice_inicial < indice_final:

    posicao_pivo_particao = particionar(vetor, indice_inicial, indice_final, imprimir)

    # Se parte à esquerda do pivô é menor, tratá-la recursivamente
    # e lidar com a parte à dreita iterativamente 'while'
    parte_esquerda_eh_menor = posicao_pivo_particao - indice_inicial < indice_final - posicao_pivo_particao

    if parte_esquerda_eh_menor:
      quick_sort_tail_2(vetor, indice_inicial, posicao_pivo_particao - 1, imprimir)

      indice_inicial = posicao_pivo_particao + 1

    # Caso contrário: recursão à direita, iteração à esquerda
    else:
      quick_sort_tail_2(vetor, posicao_pivo_particao + 1, indice_final, imprimir)

      indice_final = posicao_pivo_particao - 1



# ==================================================================================================
# Método main() - Execução de Testes     -----------------------------------------------------------

def main():

  """ Método main() - Execução de Testes """

  # Dicionário cujas chaves representam o método de ordenação escolhido
  metodos_ordenacao = {
    1 : 'BOLHA (esquerda->direita)',
    2 : 'BOLHA (direita->esquerda)',
    3 : 'INSERCAO',
    4 : 'SELECAO',
    5 : 'MESCLAGEM (nao recursivo)',
    6 : 'MESCLAGEM (recursivo)',
    7 : 'QUICKSORT (recursivo)',
    71: 'QUICK_RECURSIVO_CAUDAL_1',
    72: 'QUICK_RECURSIVO_CAUDAL_2'

  }
  # Dicionário cujas chaves representam o tipo de teste de carga escolhido
  tipos_teste = {
    1 : 'FIXO',
    2 : 'GRANDE_1_ALEATORIO',
    3 : 'GRANDE_2_ALEATORIO',
    4 : 'GRANDE_1_DECRESCENTE',
    5 : 'GRANDE_2_DECRESCENTE'
  }

  # Montando as opções dos menus
  opcoes_menu_metodo_ordenacao = dict(metodos_ordenacao)      # cópia
  opcoes_menu_metodo_ordenacao.update( { 9 : 'SAIR'} )

  opcoes_menu_tipo_teste = dict(tipos_teste)
  opcoes_menu_tipo_teste.update({
    8 : 'MUDAR_METODO',
    9 : 'SAIR'
  })


  # Armazenar as escolhas realizadas pelo usuário
  escolhas = {'metodo' : -1, 'teste' : -1}

  # OBS|=> Em Python 2.x não é possível atribuir novos valores a variáveis declaradas
  # em um escopo superior; ao tentar fazê-lo o que ocorre é declarar uma nova variável local
  # de mesmo nome. A forma que escolhemos para contornar o problema foi declarar um dicionário
  # e alterar o valor associado a chave. Escopo interno não pode fazer atribuição à variáveis
  # não locais, mas pode modificar objetos (dict) que variáveis não locais se referem.
  #
  # Os dicionários main#escolhas e o acionar_teste#vetor foram utilizados com essa finalidade.
  # Python 3 resolveu esse incoveniente sem ferir o princípio pythônico do -
  # "explicit is better than implicit", acrescentando as palavras chaves: global e nonlocal.


  # Executar Testes a Partir das Escolhas     --------------------------------------------------------

  # Esta função é utilizada meramente para fazer a interação com o usuário, logo,
  # pertence a camada de apresentação e não deve fazer parte do módulo.
  # Em função do exposto, evitamos a exposição da função #acionar_teste() fazendo
  # sua definição dentro do próprio contexto do método #main().

  def acionar_teste(escolhas):

    vetor = {'vetor': None}


    # Carregamento do Vetor ------------------------------------------------------------------------

    if escolhas['teste'] == FIXO:
      print('\nEscolheu teste VETOR {} !'.format( tipos_teste[escolhas['teste']] ))
      vetor['vetor'] = monta_vetor_FIXO( metodos_ordenacao[escolhas['metodo']] )

    elif escolhas['teste'] == GRANDE_1_ALEATORIO:
      print('\nEscolheu teste VETOR {} !'.format( tipos_teste[escolhas['teste']] ))
      vetor['vetor'] = monta_vetor_GRANDE_1_ALEATORIO( metodos_ordenacao[escolhas['metodo']] )

    elif escolhas['teste'] == GRANDE_1_DECRESCENTE:
      print('\nEscolheu teste VETOR {} !'.format( tipos_teste[escolhas['teste']] ))
      vetor['vetor'] = monta_vetor_GRANDE_1_DECRESCENTE( metodos_ordenacao[escolhas['metodo']] )

    elif escolhas['teste'] == GRANDE_2_ALEATORIO:
      print('\nEscolheu teste VETOR {} !'.format( tipos_teste[escolhas['teste']] ))
      vetor['vetor'] = monta_vetor_GRANDE_2_ALEATORIO( metodos_ordenacao[escolhas['metodo']] )

    elif escolhas['teste'] == GRANDE_2_DECRESCENTE:
      print('\nEscolheu teste VETOR {} !'.format( tipos_teste[escolhas['teste']] ))
      vetor['vetor'] = monta_vetor_GRANDE_2_DECRESCENTE( metodos_ordenacao[escolhas['metodo']] )


    # único teste que imprime os passos da ordenação
    eh_teste_fixo = escolhas['teste'] == FIXO


    # Executando os Testes - Benchmark  ------------------------------------------------------------

    # Ordenação por BOLHA (esquerda->direita)

    if escolhas['metodo'] == BOLHA_DIRETO:
      if eh_teste_fixo:
        bubble_sort(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        bubble_sort(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por BOLHA (direita->esquerda)

    elif escolhas['metodo'] == BOLHA_INVERTIDO:
      if eh_teste_fixo:
        bubble_sort_invertido(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        bubble_sort_invertido(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por INSERÇÃO

    elif escolhas['metodo'] == INSERCAO:
      if eh_teste_fixo:
        insertion_sort(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        insertion_sort(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por SELEÇÃO

    elif escolhas['metodo'] == SELECAO:
      if eh_teste_fixo:
        selection_sort(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        selection_sort(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por MESCLAGEM NÃO RECURSIVO

    elif escolhas['metodo'] == MESCLAGEM_NAO_RECURSIVO:
      if eh_teste_fixo:
        merge_sort_full_service(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        merge_sort_full_service(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por MESCLAGEM RECURSIVO

    elif escolhas['metodo'] == MESCLAGEM_RECURSIVO:
      if eh_teste_fixo:
        merge_sort_recursivo(vetor['vetor'], True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        merge_sort_recursivo(vetor['vetor'])
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por QUICKSORT (PARTIÇÃO)

    elif escolhas['metodo'] == QUICK_RECURSIVO:
      vetor = vetor['vetor']
      indice_inicial = 0
      indice_final = len(vetor) - 1
      if eh_teste_fixo:
        quick_sort(vetor, indice_inicial, indice_final, True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        quick_sort(vetor, indice_inicial, indice_final)
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por QUICKSORT CAUDAL 1 (PARTIÇÃO)

    elif escolhas['metodo'] == QUICK_RECURSIVO_CAUDAL_1:
      vetor = vetor['vetor']
      indice_inicial = 0
      indice_final = len(vetor) - 1
      if eh_teste_fixo:
        quick_sort_tail_1(vetor, indice_inicial, indice_final, True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        quick_sort_tail_1(vetor, indice_inicial, indice_final)
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )

    # Ordenação por QUICKSORT CAUDAL 2 (PARTIÇÃO)

    elif escolhas['metodo'] == QUICK_RECURSIVO_CAUDAL_2:
      vetor = vetor['vetor']
      indice_inicial = 0
      indice_final = len(vetor) - 1
      if eh_teste_fixo:
        quick_sort_tail_2(vetor, indice_inicial, indice_final, True)
      else:
        print('\nOrdenando...')
        abre_cronometro = datetime.now()
        # Aciona ordenação
        quick_sort_tail_2(vetor, indice_inicial, indice_final)
        fecha_cronometro = datetime.now()
        diferenca = fecha_cronometro - abre_cronometro
        print('            Levou {:.3f} segundos para calcular\n'.format(diferenca.total_seconds()) )


  # Loop Principal do Programa    ------------------------------------------------------------------
  # Interação com o usuário através do menu de opções

  while True:
    # Escolha do método de ordenação a ser executado
    escolhas['metodo'] = escolhe_metodo()

    if escolhas['metodo'] not in opcoes_menu_metodo_ordenacao:
      print('\nOpção INVÁLIDA !  Tente novamente...\n')

    elif not escolhas['metodo'] == SAIR:
      while True:
        # Escolha do tipo de teste a ser executado
        escolhas['teste'] = escolhe_teste()

        if escolhas['teste'] == MUDAR_METODO:
          print('\nEscolheu voltar à escolha do método de ordenação !')
          break

        elif escolhas['teste'] == SAIR:
          print('\nEscolheu SAIR !\n\n')
          escolhas['metodo'] = SAIR   # deixar o loop externo saber da intenção
          break

        elif escolhas['teste'] not in opcoes_menu_tipo_teste:
          print('\nOpção INVÁLIDA !  Tente novamente...\n')

        else:
          acionar_teste(escolhas)

    # Se pediu pra sair no loop interno, obedeça e saia da execução do programa
    if escolhas['metodo'] == SAIR:
      break

# Boa educação
if __name__ == '__main__':
  main()
