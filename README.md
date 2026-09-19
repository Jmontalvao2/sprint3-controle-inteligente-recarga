# SPRINT 3 - CONTROLE INTELIGENTE DE SESSAO DE RECARGA

## Integrantes

* RM 569914
* RM 572738
* RM 571630
* RM 570619
* RM 572679

---

## 1. DESCRICAO DO PROJETO

Este projeto apresenta um prototipo educacional de um sistema inteligente de controle de sessao de recarga, desenvolvido utilizando o Raspberry Pi Pico e a linguagem MicroPython.

O sistema simula uma residencia que possui uma determinada geracao de energia e um determinado consumo. A partir desses valores, o Raspberry Pi Pico calcula a energia disponivel para uma possivel sessao de recarga.

O projeto foi inspirado no conceito de gerenciamento inteligente de energia, utilizando como referencia conceitual a ideia de controladores inteligentes de energia.

---

## 2. OBJETIVO

O objetivo do projeto e demonstrar, na pratica, a relacao entre entrada de dados, processamento, memoria e saida dentro de um sistema computacional.

O Raspberry Pi Pico recebe valores simulados de geracao e consumo, realiza o processamento desses dados e determina automaticamente o estado da sessao de recarga.

---

## 3. FUNCIONAMENTO

A energia disponivel e calculada utilizando a seguinte formula:

ENERGIA DISPONIVEL = GERACAO - CONSUMO

Depois do calculo, o sistema verifica a quantidade de energia disponivel e determina um dos tres estados:

### LED VERDE - RECARGA AUTORIZADA

Quando a energia disponivel e igual ou superior a 2000 W.

### LED AMARELO - RECARGA REDUZIDA

Quando a energia disponivel e maior que 0 W e menor que 2000 W.

### LED VERMELHO - RECARGA BLOQUEADA

Quando a energia disponivel e igual ou inferior a 0 W.

---

## 4. SITUACOES TESTADAS

### Situacao 1 - Energia suficiente

Geracao: 4000 W

Consumo: 1500 W

Energia disponivel:

4000 - 1500 = 2500 W

Resultado:

RECARGA AUTORIZADA

LED verde aceso.

---

### Situacao 2 - Energia limitada

Geracao: 1800 W

Consumo: 1500 W

Energia disponivel:

1800 - 1500 = 300 W

Resultado:

RECARGA REDUZIDA

LED amarelo aceso.

---

### Situacao 3 - Energia insuficiente

Geracao: 1000 W

Consumo: 1800 W

Energia disponivel:

1000 - 1800 = -800 W

Resultado:

RECARGA BLOQUEADA

LED vermelho aceso.

---

## 5. HARDWARE

O prototipo utiliza:

* Raspberry Pi Pico
* LED verde
* LED amarelo
* LED vermelho
* Resistores para os LEDs
* Protoboard
* Jumpers

### Ligacao dos LEDs

LED verde: GP2

LED amarelo: GP3

LED vermelho: GP4

---

## 6. SOFTWARE

O projeto foi desenvolvido utilizando:

* MicroPython
* Raspberry Pi Pico
* Wokwi

O Wokwi foi utilizado para simular o funcionamento do circuito e permitir a demonstracao dos tres estados de recarga.

---

## 7. ARQUITETURA DE COMPUTADORES

O projeto pode ser relacionado aos conceitos de Arquitetura de Computadores por meio do fluxo:

ENTRADA -> PROCESSAMENTO -> MEMORIA -> SAIDA

### Entrada

Os valores de geracao e consumo representam os dados de entrada do sistema.

### Processamento

O Raspberry Pi Pico executa o programa em MicroPython e realiza o calculo:

GERACAO - CONSUMO

Depois, o processador compara o resultado com os limites definidos para determinar o estado da recarga.

### Memoria

Durante a execucao, os valores de geracao, consumo e energia disponivel sao armazenados em variaveis na memoria do sistema.

### Saida

Os LEDs representam os dispositivos de saida.

O sistema tambem apresenta no terminal os valores de geracao, consumo, energia disponivel e o estado da recarga.

---

## 8. REPRESENTACAO DE DADOS

Um dos valores utilizados pelo sistema pode ser representado em diferentes sistemas numericos.

Exemplo utilizando 2500 W:

Decimal:

2500

Binario:

100111000100

Hexadecimal:

9C4

Essa representacao demonstra que um mesmo valor pode ser armazenado e processado pelo computador utilizando diferentes bases numericas.

---

## 9. LOGICA DO PROGRAMA

O programa primeiro configura os tres LEDs como dispositivos de saida.

Depois, uma funcao recebe os valores de geracao e consumo.

O sistema calcula a energia disponivel subtraindo o consumo da geracao.

Em seguida, utiliza estruturas condicionais para determinar qual LED deve ser ligado.

Se a energia disponivel for igual ou superior a 2000 W, o LED verde e acionado.

Se a energia disponivel estiver entre 1 W e 1999 W, o LED amarelo e acionado.

Se a energia disponivel for igual ou inferior a 0 W, o LED vermelho e acionado.

Os valores tambem sao apresentados no terminal para facilitar a visualizacao da sessao de recarga.

---

## 10. RESULTADO

O prototipo demonstra que o Raspberry Pi Pico consegue receber dados, processa-los e gerar uma resposta de acordo com as condicoes programadas.

As tres situacoes de recarga sao representadas visualmente pelos LEDs verde, amarelo e vermelho.

Dessa forma, o projeto demonstra a integracao entre hardware, software e dados.

---

## 11. SIMULADOR

O projeto foi desenvolvido e testado no simulador Wokwi.

Link do projeto:

https://wokwi.com/projects/475635833842384897

---

## 12. VIDEO

Link do video no YouTube:

COLOCAR LINK DO YOUTUBE AQUI
