# Lei de *Amdahl*

## Conceitos fundamentais

- **Speedup** (aceleração): impacto na **latência** do processamento.
- **Velocidade**: O tempo total de processamento.

A expressão matemática de *Amdahl* mede o **ganho** ao se utilizar múltiplos processadores:
$S=\dfrac{T(1)}{T(N)},$
onde T é o tempo de execução com processadores
e N é o número de processadores

Assumir que uma **fração B** do programa que é **estritamente sequencial.** Carregar a biblioteca, por exemplo faz parte da fração B. Portanto o complemento da fração B (1-B) é o trecho que pode ser colocado em paralelo.

O tempo total de execução com paralelismo é: 
$$
T(N)=B.T(1)+\dfrac{(1-B).T(1)}{N}
$$
ou seja: A parte sequencial mais a parte paralela

Aplicando uma fórmula na outra temos:

$$
S=\dfrac{T(1)}{B.T(1)+\dfrac{(1-B).T(1)}{N}}
$$

$$
S=\dfrac{1}{B+\dfrac{1-B}{N}}
$$

---
### Exemplo 1:
Se 40% de um programa pode ser paralelizado ($1-B=0,4$ e $B=0,6$) e utilizamos 4 processadores ($N=4$), qual será o ganho?
$$
S=\dfrac{1}{0,6+\dfrac{0,4}{4}}=\dfrac{1}{0,7} \approx 1,43
$$
Temos um ganho $S$ de aproximadamente **43%** de eficiência

---
### Exemplo 2:
Agora, suponha que o programa seja reestruturado para permitir que 80% seja executado em paralelo, e que rode utilizando apenas dois núcleos. Qual é o ganho?
$$
S=\dfrac{1}{0,2+\dfrac{0,8}{2}}=\dfrac{1}{0,6} = 1,66
$$
Temos um ganho $S$ de **66%** de eficiência.

Portanto, **o número de núcleos (processadores) não garante** necessariamente uma melhor eficiência.

---
### Exemplo 3:
Se $B=0,1$, com um número *infinito de processadores*, qual o ganho máximo?
$$
\lim_{N \to \infty} S=S=\dfrac{1}{0,1+\dfrac{0,9}{\infty}}=\dfrac{1}{0,1} = 10
$$
Portanto, existe um limite de **ganho máximo**

---
### Exemplo 4:
Considere um sistema de renderização gráfica 3D. Suponha que 95% da tarefa de renderização pode ser paralelizada. Se usarmos 8 processadores, qual o valor do ganho?
$$
S=\dfrac{1}{0,05+\dfrac{0,95}{8}}=\dfrac{1}{0,16875} \approx 5,9259
$$
---