import numpy as np
from scipy.stats import binom
import networkx as nx
import matplotlib.pyplot as plt
T =1
S=100
K=95
v=0.2
r =0.05
n = 10000
clase = 1 #1 para call -1 para put
tipo = 0 #1 Americana 0 Europea
#------------------------------

def opergen(n):
    delta=T/n
    u =np.exp(v*np.sqrt(delta))
    d=1/u
    p =(np.exp(r*delta)-d)/(u-d)
    return [delta,u,d,p]

#------------------------------


def BinomialRapida(n):

    delta,u,d,p =opergen(n)

    Sn=S*np.geomspace(u**n,d**n,n+1)
    payoff=np.maximum (0,(Sn-K)*clase)
    prima =[binom.pmf(n-i,n,p) for i in range(n+1)]
    prima=payoff*np.array(prima)
    prima=np.exp(-r*T)*prima.sum()
    return prima

#------------------------------

import numpy as np
from scipy.stats import norm

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)

#------------------------------

def BinomialLenta(n):
    delta,u,d,p =opergen(n)
    pre = np.exp(-r*delta)

    Sn =[S*np.geomspace(u**i,d**i,i+1)
         for i in range(n+1)]
    payoff=[np.maximum (0,(Sn[i]-K)*clase) for i in range(n+1)]

    pay = payoff.copy()  # Inicializamos con el payoff final

    for j in range(n):
        if tipo==1:
           pay[n-j-1] =[max(payoff[n-j-1][i],(p * pay[n-j][i] + (1 - p) * pay[n-j][i + 1]) * pre)
                     for i in range(n - j)]
        else:
           pay[n-j-1] =[(p * pay[n-j][i] + (1 - p) * pay[n-j][i + 1]) * pre
                     for i in range(n - j)]


    return [pay[0][0],Sn,pay]

#------------------------------

def BinomialGrafica(n):
    delta,u,d,p =opergen(n)
    pre = np.exp(-r*delta)

    Sn =[S*np.geomspace(opergen(i)[1]**i,opergen(i)[2]**i,i+1)
         for i in range(1,n+1)]
    payoff=[np.maximum (0,(Sn[i]-K)*clase) for i in range(n)]
    prima =[[binom.pmf(j-i,j,p=opergen(j)[3]) for i in range(j+1)] for j in range(1,n+1)]

    for i in range(n):
        prima[i]=payoff[i]*np.array(prima[i])
        prima[i]=np.exp(-r*T)*prima[i].sum()
    return prima

#------------------------------

def graficoConvergencia():
    Y=BinomialGrafica(1000)
    import matplotlib.pyplot as plt
    It=len(Y)+1
    x=list(range(1,It))
    z=(It-1)*[float(BS_CALL(S, K, T, r, v))]
    plt.scatter(x,Y, s=0.01)
    plt.plot(x,Y)
    plt.plot(x,z)
    plt.show()

#------------------------------

from mpmath import mp, binomial, exp, sqrt, mpf

def BinomialRp(n):
    delta, u, d, p = opg(n)

    Sn = [S * u**i * d**(n-i) for i in range(n+1)]
    payoff = [mpf(max(0, (Sn[i]-K) * clase)) for i in range(n+1)]

    prima = [binomial(n, i) * p**i * (1-p)**(n-i) for i in range(n+1)]

    prima = [exp(-r*T) * payoff[i] * prima[i] for i in range(n+1)]

    return sum(prima)

def opg(n):
    delta =mpf( T / n)
    u = exp(v * sqrt(delta))
    d = 1 / u
    p = (exp(r * delta) - d) / (u - d)
    return delta, u, d, p

#------------------------------
def grafico(arbol,n):
    # Crea un grafo dirigido
    G = nx.DiGraph()

# Diccionario para rastrear nodos duplicados
    nodo_counter = {}
    label =[]
# Agrega nodos
    for i in range(n+1):
        label.append([])
        for j in range(len(arbol[i])):
            valor_nodo = round(arbol[i][j], 2)

        # Agrega un sufijo único para evitar duplicados
            if valor_nodo in nodo_counter:
               nodo_counter[valor_nodo] += 1
               aux =nodo_counter[valor_nodo]*" "
               nombre_nodo = f"{aux}{valor_nodo}{aux}"
            else:
               nodo_counter[valor_nodo] = 0
               aux =nodo_counter[valor_nodo]*" "
               nombre_nodo = f"{aux}{valor_nodo}{aux}"

            G.add_node(nombre_nodo)
            label[i].append(nombre_nodo)

# Agrega arcos (conexiones entre nodos)
    for i in range(n):
        for j in range(len(arbol[i])):
            nodo_actual = label[i][j]
            nodo_siguiente_izquierda = label[i+1][j]
            nodo_siguiente_derecha = label[i+1][j+1]

            G.add_edge(nodo_actual, nodo_siguiente_izquierda)
            G.add_edge(nodo_actual, nodo_siguiente_derecha)

# Dibuja el grafo
    pos = {}
    for i in range(n+1):
        paso = (2*i)/len(arbol[i])
        for j in range(len(arbol[i])):
            nombre_nodo = label[i][j]
            pos[nombre_nodo] = (i, i - paso*j)

# Define la disposición de los nodos

    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold")

    plt.show()

#------------------------------

def Binomial(n):
    tipos ={-1:"Put",1:"Call"}
    if n<11 or tipo==1:
       prima,arbol,arbolOp =BinomialLenta(n)
       if n<11:
          grafico(arbol,n)
          grafico(arbolOp,n)
    elif n<10**3:
       prima =BinomialRapida(n)
    else:
       prima=BinomialRp(n)
    return f"el valor del {tipos[clase]} es {prima}"