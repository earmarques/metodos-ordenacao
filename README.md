# Métododos de Ordenação
Programa didático com testes de desempenho para os métodos de ordenação implementados em `Python 2` : <kbd>bubble sort</kbd>, <kbd>insertion sort</kbd>, <kbd>merge sort</kbd>, <kbd>quick_sort</kbd> e <kbd>selection_sort</kbd>. 
<br>
Programadores mais experientes podem achar exagerado a quantidade de comentários, mas o público alvo são estudantes que estão começando na programação, que não têm nem domínio pleno da linguagem Python nem maturidade em raciocinar na lógica de programação, por isso fizemos um descrição detalhada do código. 

### Contexto

Terceiro semestre na Fatec, disciplina Estrutura de Dados ministrada pelo querido mestre Professor Dr. Carlos Magnus Carlson Filho. Simplesmente o melhor curso de Estrutura de Dados da galáxia. Ao professor Carlos fica a eterna gratidão de um eterno aprendiz, obrigado Mestre.

A parte I do curso é toda em linguagem C, não há nada como C para entender alocação de memória e como as coisas num nível mais elementar se organiza. A Fatec tem a preocupação de se alinhar ao mercado, então vimos Python, uma linguagem em alta e gostosa de programar que nos foi apresentada no semestre anterior pelo Professor Dr. Dezani. Logo, na breve parte II do curso de Estrutura de Dados tivemos uma revisão de Python, para posteriormente seguir com a parte III onde veríamos filas, pilhas, listas ligadas, árvores binárias etc.

Pois bem, na ocasião em que estávamos vendo filas e pilhas, pilha de chamadas a métodos, o Professor foi abordar a elegante <em>programação recursiva</em>. É aqui que nasce este repositório. O Professor nos forneceu uma implementação de algoritmos de ordenaçao escrito em C. Já havia algumas semanas que estavamos brincando com Python, já estávamos "bem acostumados" com as mordomias de uma linguagem moderna e de repente voltamos a esculpir conceitos no machado. Me soou como uma quebra de simetria.

O que fiz foi passar o programa em C do Carlos para Python 2 (a versão da máquina do Professor). No aspecto visual está absolutamente igual, mesma saída, mesma interação com o usuário. Agora o professor Carlos não precisa mais revisitar a linguagem C do início do curso, pode permanecer em Python tratando dos conceitos elementares e comuns a qualquer linguagem.

---
## Apresentação

### Algoritmo de Ordenação

* Primeiro se escolhe o método de ordenação.

<img width=70% alt="Menu 1 - escolha do método de ordenação" title="Menu 1 - escolha do método de ordenação" src= "https://github.com/earmarques/metodos-ordenacao/blob/main/images/menu1.png" /><br>
<sup>_Figura 1: Menu 1, escolha do método de ordenação_</sup>

Veja que temos mais de um tipo de implementação para o mesmo método. <kbd>bubble sort</kbd> tem o normal direto e o invertido. O de mesclagem (<kbd>merge sort</kbd>) tem o recursivo e o não recursivo. Para o meu preferido <kbd>quick sort</kbd> fiz três implementações e acredito ser necessário dar mais informações sobre esse métodos e suas variações. 

A primeira implementação (opção 7) é a tradicional, como o método foi inicialmente concebido. Nela o algoritmo mergulha em recorrência sempre pelo particionamento à esquerda do pivô e quando bate no fundo pula para o particionamento à direita do pivô e depois vem subindo nos particionamentos e fazendo o lado direito. Isso é ruim porque se empilha demais, faz muitas chamadas em recorrência. O pior cenário é quando temos vetores ordenados em ordem decrescente. Com um vetor assim, o algoritmo tem de inverter totalmente o vetor e para tanto faria muita recorrência, ocasionando o estouro da pilha (_stack over flow_).

A segunda implementação do _quick sort_ está na opção 71. Nela a recursividade ocorre em uma partição de cada vez, o que requer um empilhamento de chamadas menor. Ainda assim, no vetor de teste descrescente de 20.000 elementos já há o derramamento da pilha. No _quick sort tail1_ a recorrência sempre entra pelo mesmo lado, no caso, pelo particionamento à esquerda do pivô. Na realidade, o _quick sort_ da opção 71 é uma preparação para o estudante compreender o _quick sort tail2_.

A terceira implementação do _quick sort_ da opção 72 é a única em que não ocorre o estouro da pilha de chamadas, mesmo para o vetor descrescente de 40.000 elementos. O _quick sort tail2_ é uma melhoria do caudal 1, com um critério mais inteligente. Nele a recursividade desce sempre pelo menor particionamento. Depois de encontrar a posição correta do pivô compare-se o tamanho de cada lado e se faz a recorrência na partição menor. Dessa forma, além de atacar apenas uma partição por vez, ataca-se a partição menor, sendo assim, o mergulho na recursividade não é tão fundo, retorna-se mais rápido pois a pilha de chamada é mais rasa, é menor.

### Teste de carga (_Benchmark_)

* Após a escolha do algoritmo de ordenação temos um segundo menu para fazermos a escolha do teste de carga ao qual o algoritmo será submetido.

<img width=70% alt="Escolha do tipo de teste" title="Escolha do tipo de teste" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/menu2.png"><br>
<sup>_Figura 2: Menu 2, escolha do tipo de teste_</sup>


#### Opção 1. Validação do método
A opção 1 é uma inspeção visual do comportamento do método. 
<br>
Sempre usamos o mesmo vetor de oito elementos e imprimimos todos os passos da ordenação. Dessa forma, fica fácil checar as movimentações dos elementos pelo algorítmo e comparar seu _modus operandi_ com os demais métodos.
Na figura a seguir, vemos as permutas dos elementos realizadas pelo <kbd>bubble sort</kbd> a cada passada do loop. Mentalmente visualizamos a bolha ao redor número 11, o 5° elemento do vetor, deslocando-o para o início do vetor a cada passo.

<img width=70% alt="Validação do método" title="Validação do método" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/validacao_algoritmo.png"><br>
<sup>_Figura 3: Bubble sort, etapas da ordenação_</sup>


#### Opções 2 e 3. Vetores Aleatórios

Nas opções 2 e 3 criamos vetores de 20 mil e 40 mil, respectivamente, com valores tomados aleatóriamente. 
<br>
Aplicamos o método de ordenação escolhido e mostramos o tempo necessário para completar a ordenação.  Com esses vetores o estudante pode fazer a comparação de desempenho entre os algoritmos, comparando os tempos de um e de outro. Por exemplo, aplicamos o método de ordenação _bubble sort_ a um vetor randômico de 40 mil elementos e o resultado está na figura 4. Na figura 5 temos o desempenho do _quick sort tail 2_ para um vetor semelhante, de 40 mil elementos gerados aleatóriamente.

<img width=70% alt="Bubble sort - 40 mil randômico" title="Bubble sort - 40 mil randômico" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/bubble-40mil-random.png" ><br>
<sup>_Figura 4: Desempenho do bubble sort_</sup>

<img width=70% alt="Quick sort - 40 mil randômico" title="Quick sort - 40 mil randômico" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_40mil-random.png" ><br>
<sup>_Figura 5: Desempenho do quick sort recursivo_</sup>

Nesse caso específico, enquanto o _bubble sort_ levou 84 segundos para ordenar o vetor, o _quick sort_ levou apenas 5 centésimos de segundo. Mostrando que o método da bolha é pop, talvez o mais famoso, mas tem um desempenho sofrível. 

#### Opções 4 e 5. Vetores Decrescentes

Nas opções 4 e 5 criamos vetores de 20 mil e 40 mil, respectivamente, com valores já ordenandos, mas em ordem decrescente. Nesta situação, o método de ordernação tem de inverter totalmente o vetor e isso pode ser extremamente custoso em recursos computaionais para alguns algoritmos.
<br>
Um exemplo está na figura 6. Escolhemos no menu a opção 7.1, um tipo de implementação do _quicksort recursivo_ em que estora a pilha de chamadas. Já com a segunda forma de implementar o _quicksort_ recursivamente da opção 7.2 o estouro não acontece.

<img width=80% alt="Quicksort recursivo - 40mil stackOverFlow" title="Quicksort recursivo - 40mil stackOverFlow" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_op7-stackoverflow.png" /><br>
<sup>_Figura 6a: Estouro da pilha de chamada_</sup>

<img width=80% alt="Quicksort recursivo - 40mil stackOverFlow 2" title="Quicksort recursivo - 40mil stackOverFlow 2" src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/quick_op7-stackoverflow2.png" /><br>
<sup>_Figura 7b: Estouro da pilha de chamada_</sup>

---

## Dependência
Precisa do Python 3 instalado. Se usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão.
Verifique com o comando:
```sh
python --version
```
<kbd>_Output: Python 3.10.6_</kbd>

Caso não esteja instalado, instale com os comandos abaixo:
```sh
sudo apt update
```
```sh
sudo apt install python3
```

---

## Executar

### Com o comando python
Baixe o arquivo metodos_ordenacao.py e no mesmo diretório execute-o comando:

```sh
python metodos_ordenacao.py
```
### Como shell script
Baixe o arquivo metodos_ordenacao.py e forneça permissão de execução ao arquivo:

```sh
chmod +x metodos_ordenacao.py
```
E execute com:
```sh
./metodos_ordenacao.py
```

Se encontrar algum erro na linha 1 devido a `#!/usr/bin/env python3` dê o comando 
```sh
whereis python
```
E corrija o path do python pela saída do whereis, ficaria algo assim: #!/usr/bin/python


### Colab
Pode executar no próprio navegar usando o Google Colab <a href="https://colab.research.google.com/"><img src="https://github.com/earmarques/metodos-ordenacao/blob/main/images/colab.png" alt="Google Colab" title="Google Colab"></a>. Crie um novo notebook e cole o código de <kbd>metodos_ordenacao.py</kbd> e aperte o play.

  
