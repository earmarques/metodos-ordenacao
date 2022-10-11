# Métododos de Ordenação
Programa didático com testes de desempenho para os métodos de ordenação implementados em `Python 2` : <kbd>bubble sort</kbd>, <kbd>insertion sort</kbd>, <kbd>merge sort</kbd>, <kbd>quick_sort</kbd> e <kbd>selection_sort</kbd>. 

### Contexto

Terceiro semestre na Fatec, disciplina Estrutura de Dados ministrada pelo querido mestre Professor Dr. Carlos Magnus Carlson Filho. Simplesmente o melhor curso de Estrutura de Dados da galáxia. Ao professor Carlos fica a eterna gratidão de um eterno aprendiz, obrigado Mestre.

A parte I do curso é toda em linguagem C, não há nada como C para entender alocação de memória e como as coisas num nível mais elementar se organiza. A Fatec tem a preocupação de se alinhar ao mercado, então vimos Python, uma linguagem em alta e gostosa de programar que nos foi apresentada no semestre anterior pelo Professor Dr. Dezani. Logo, na breve parte II do curso de Estrutura de Dados tivemos uma revisão de Python, para posteriormente seguir com a parte III onde veríamos filas, pilhas, listas ligadas, árvores binárias etc.

Pois bem, na ocasião em que estávamos vendo filas e pilhas, pilha de chamadas a métodos, o Professor foi abordar a elegante <strong><em>programação recursiva</em></strong>. É aqui que surge este repositório. O Professor nos forneceu uma implementação de algoritmos de ordenaçao escrito em C. Já havia algumas semanas que estavamos brincando com Python, já estávamos 'bem acostumados' com as mordomias de uma linguagem moderna e de repente voltamos a esculpir conceitos no machado. Me soou como uma quebra de simetria.

O que fiz foi passar o programa em C do Carlos para Python 2 (a versão da máquina do Professor). No aspecto visual está absolutamente igual, mesma saída, mesma interação com o usuário. Agora o professor Carlos não precisa mais revisitar a linguagem C do início do curso, pode permanecer em Python tratando dos conceitos elementares e comuns a qualquer linguagem.

---
## Apresentação

### Algoritmo de Ordenação

* Primeiro se escolhe o método de ordenação.

<img width=70% alt="Menu 1 - escolha do método de ordenação" title="Menu 1 - escolha do método de ordenação" src= "https://github.com/earmarques/metodos-ordenacao/blob/main/images/menu1.png" /><br>
<sup>_Figura 1: Menu 1, escolha do método de ordenação_</sup>

Veja que temos mais de um tipo de implementação para o mesmo método. <kbd>Bubble sort</kbd> tem o normal direto e o invertido. O de mesclagem (<kbd>merge sort</kbd>) tem o recursivo e o não recursivo. Para o meu preferido fiz três implementações. Detalhes de implementação podem ser visto no [código](https://github.com/earmarques/metodos-ordenacao/blob/main/MetodosOrdenacao.py) ou comentada na documentação [wiki](https://github.com/earmarques/metodos-ordenacao/wiki) do repositório.


### Teste de carga (Benchmark)

* Após a escolha do algoritmo de ordenação temos um segundo menu para fazermos a escolha do teste de carga ao qual o algorítmo será submetido.

<img width=70% alt="Escolha do tipo de teste" title="Escolha do tipo de teste" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/menu2.png"><br>
<sup>_Figura 2: Menu 2, escolha do tipo de teste_</sup>


#### Opção 1. Validação do método
A opção 1 é uma inspeção visual do comportamento do método. Sempre usamos o mesmo vetor de oito elementos e imprimimos todos os passos da ordenação. Dessa forma fica fácil checar as movimentações dos elementos pelo algorítmo e comparar seu _modus operandi_ com os demais métodos.
Na figura a seguir, vemos as permutas dos elementos realizadas pelo <kbd>bubble sort</kbd> a cada passada do loop. Mentalmente visualizamos a bolha ao redor número 11, o 5° elemento do vetor, deslocando-o para o início do vetor a cada passo.

<img width=70% alt="Validação do método" title="Validação do método" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/validacao_algoritmo.png"><br>
<sup>_Figura 3: Bubble sort, etapas da ordenação_</sup>


#### Opções 2 e 3. Vetores Aleatórios

Nas opções 2 e 3 criamos vetores de 20 mil e 40 mil, respectivamente, com valores tomados aleatóriamente. E aplicamos o método de ordenação escolhido e mostramos tempo necessário para completar a ordenação.  Com esses vetores o estudante pode fazer a comparação de desempenho entre os algoritmos comparando os tempos de um e de outro. Por exemplo, aplicamos o método de ordenação _bubble sort_ a um vetor randômico de 40 mil elementos e o resultado está na figura 4. Na figura 5 temos o desempenho do _quick sort tail 2_ para um vetor semelhante, de 40 mil elementos gerados aleatóriamente.

<img width=70% alt="Bubble sort - 40 mil randômico" title="Bubble sort - 40 mil randômico" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/bubble-40mil-random.png" ><br>
<sup>_Figura 4: Desempenho do bubble sort_</sup>

<img width=70% alt="Quick sort - 40 mil randômico" title="Quick sort - 40 mil randômico" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_40mil-random.png" ><br>
<sup>_Figura 5: Desempenho do quick sort recursivo_</sup>

Nesse caso específico, enquanto o bubble sort levou 84 segundos para ordenar o vetor, o quick sort levou apenas 5 centésimos de segundo


<img width=80% alt="Quicksort recursivo - 40mil stackOverFlow" title="Quicksort recursivo - 40mil stackOverFlow" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_op7-stackoverflow.png" /><br>
<sup>_Figura : _</sup>

<img width=80% alt="Quicksort recursivo - 40mil stackOverFlow 2" title="Quicksort recursivo - 40mil stackOverFlow 2" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_op7-stackoverflow2.png" /><br>
<sup>_Figura : _</sup>


<img width=70% alt="" title="" src="" />
<img width=70% alt="" title="" src="" />
<img width=70% alt="" title="" src="" />
<img width=70% alt="" title="" src="" />
<img width=70% alt="" title="" src="" />
<img width=70% alt="" title="" src="" />

  
