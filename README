# Ajuste de Curvas - Método dos Mínimos Quadrados (MMQ)

Este projeto implementa o Método dos Mínimos Quadrados (MMQ) em Python para realizar regressões lineares simples (ajuste de curvas de primeira ordem). O algoritmo é capaz de ler dados empíricos, montar o sistema linear de Equações Normais e resolvê-lo utilizando o método numérico de Eliminação de Gauss com Pivotamento Parcial.

## Funcionalidades

* **Entrada Dinâmica:** Aceita a inserção de vetores numéricos de qualquer tamanho.
* **Resolução Estável:** Utiliza Eliminação de Gauss com pesquisa do maior pivô para minimizar erros de arredondamento.
* **Métricas de Qualidade:** Calcula o Coeficiente de Determinação ($R^2$) e a Variância Residual ($\sigma^2$) para validar a precisão matemática do modelo.
* **Visualização Gráfica:** Plota automaticamente a dispersão dos dados experimentais e a reta teórica ajustada utilizando a biblioteca Matplotlib.

## Pré-requisitos

Para executar este projeto, certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:
* `numpy` (Para as matrizes, somatórios e processamento algébrico)
* `matplotlib` (Para a plotagem do gráfico final)

## Como Utilizar

1. Execute o ficheiro principal (`main.py`) no terminal.
2. Insira a quantidade total de pontos recolhidos no experimento.
3. Digite os valores do eixo X separados por um espaço em branco.
4. Digite os valores do eixo Y separados por um espaço em branco.

### Exemplo de Teste

Para validar a integridade do algoritmo, pode utilizar os seguintes dados de calibração:
* **Quantidade de pontos:** 5
* **Valores de X:** `0.3 2.7 4.5 5.9 7.8`
* **Valores de Y:** `1.8 1.9 3.1 3.9 3.3`

**Resultados Esperados:**
* **Coeficientes:** $b_0 = 1.6560$ e $b_1 = 0.2698$
* **Equação da reta:** $y(x) = 1.6560 + 0.2698x$
* **Qualidade:** $R^2 \approx 0.7235$ e Variância Residual $\approx 0.3096$