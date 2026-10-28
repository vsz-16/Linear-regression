import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Planilha(caminho):

    if caminho.endswith('.csv'):
        df = pd.read_csv(caminho, header=None)
    else:
        df = pd.read_excel(caminho, header=None)
    
    # Pega as duas primeiras colunas do arquivo
    colx = df.iloc[:, 0]
    coly = df.iloc[:, 1]
    
    # Força a conversão para número
    # Textos, títulos e legendas viram NaN
    xnum = pd.to_numeric(colx, errors='coerce')
    ynum = pd.to_numeric(coly, errors='coerce')
    
    # Junta as duas colunas e remove todas as linhas que contêm NaN com o dropna()
    tabela_limpa = pd.DataFrame({'X': xnum, 'Y': ynum}).dropna()
    
    # Extrai os vetores prontos em formato float do NumPy
    x = tabela_limpa['X'].to_numpy(dtype=float)
    y = tabela_limpa['Y'].to_numpy(dtype=float)
    
    return x, y

def Entrada():
    print("Como quer inserir os dados?")
    print("1 - Digitar")
    print("2 - Carregar ficheiro (CSV ou Excel)")
    op = input("Digite o número escolhido:\n")
    
    if op == '1':
        n = int(input("Quantos pontos você tem?\n"))
        x = np.array(input(f"Digite os {n} valores de X:\n").split(), dtype=float)
        y = np.array(input(f"Digite os {n} valores de Y:\n").split(), dtype=float)
        return x, y
    elif op == '2':
        caminho = input("Cole o caminho do ficheiro (ex: dados.csv):\n ")
        return Planilha(caminho)
    else:
        print("Opção inválida.")
        return Entrada()

#Organizar a matriz e o sistema linear
def Ajuste(x, y):
    n = len(x)
    xi = np.sum(x) #Somatório dos valores do vetor x
    xi2 = np.sum(x**2) #Somatório dos valores do vetor x²
    yi = np.sum(y) #Somatório dos valores do vetor y
    yixi = np.sum(y*x) #Somatório dos valores de x*y

    #Matriz aumentada:
    matriz = np.array([[n, xi, yi], [xi, xi2, yixi]], dtype = float)

    return matriz

def Pivot(matriz, m = 2):
    #Salvando a matriz pra usar no calculo do resíduo depois
    Aoriginal = np.copy(matriz[:, :m])
    boriginal = np.copy(matriz[:, m])

    for i in range(m - 1):
        # Variáveis auxiliares para encontrar o maior pivô na coluna 'i'
        maior = np.abs(matriz[i, i])
        lmaior = i
        
        # Procura o maior número em módulo na coluna da linha i+1 em diante
        for k in range(i + 1, m):
            if np.abs(matriz[k, i]) > maior:
                maior = np.abs(matriz[k, i])
                lmaior = k
                
        # Teste e troca de linhas
        if maior == 0:
            print(f"Erro: A coluna {i} tem apenas zeros. A matriz não é válida.")
            return
        elif lmaior != i:
            matriz[[i, lmaior]] = matriz[[lmaior, i]]
            
        # Zerando tudo
        for j in range(i + 1, m):
            a = matriz[j, i] / matriz[i, i]
            matriz[j] = matriz[j] - a * matriz[i]
            
#Resolvendo o sistema
    x = np.zeros(m)
    for l in range(m - 1, -1, -1):
        soma = matriz[l, m] 
        
        for n in range(l + 1, m):
            soma = soma - (matriz[l, n] * x[n])
            
        x[l] = soma / matriz[l, l]
    print(f"\n Os valores de b0 e b1 são: {x}\n")
    print(f"Portanto a equação seria: {x[0]:.4} + {x[1]:.4}x\n")

    #Calculo do resíduo
    residuo = boriginal - np.dot(Aoriginal, x)
    erro = np.linalg.norm(residuo)
    print("--- Análise de Erro ---")
    print(f"Vetor Resíduo: {residuo}")
    print(f"Magnitude do Erro: {erro:.2e}\n")

    return x

def Qualidade(x, y, b0, b1):
    n = len(x)
    p = 2 # Número de parâmetros da reta (b0 e b1)
    
    #Vetor de valores previstos pelo modelo matemático (Ui)
    U = b0 + b1 * x
    
    # Soma dos Quadrados Residuais (SQresidual ou D)
    SQresidual = np.sum((y - U)**2)
    
    # Soma de Quadrados Totais usando a fórmula expandida
    somay = np.sum(y)
    SQtotal = np.sum(y**2) - (1/n) * (somay**2) 
    
    # Coeficiente de Determinação (R²)
    R2 = 1 - (SQresidual / SQtotal)
    
    # Variância residual (sigma²)
    sigma2 = SQresidual / (n - p) #[cite: 13]
    
    print("\n--- Qualidade do Ajuste ---")
    print(f"Coeficiente de Determinação (R²): {R2:.4f}")
    print(f"Variância Residual (σ²): {sigma2:.4f}\n")
    
    return R2, sigma2

def Grafico(x, y, b0, b1):
    U = b0 + b1 * x
    
    # Plota os dados como pontos
    plt.scatter(x, y, color='red', label='Dados Empíricos')
    
    # Plota a reta teórica calculada pelo MMQ
    plt.plot(x, U, color='blue', label=f'Ajuste: U(x) = {b0:.4f} + {b1:.4f}x')
    
    plt.title('Método dos Mínimos Quadrados - Regressão Linear')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.show()

def main():
    x, y = Entrada()
    matriz = Ajuste(x, y)
    b0, b1 = Pivot(matriz)
    Qualidade(x, y, b0, b1)
    Grafico(x, y, b0, b1)

main()