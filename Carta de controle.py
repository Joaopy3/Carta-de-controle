import numpy as np,os,matplotlib.pyplot as plt
from pathlib import Path

def carta_controle(array,caminho,li,ls):

    posicoes = np.arange(1, len(array) + 1)
    desvio_padrao = np.std(array)
    fig, ax = plt.subplots(figsize=(16,4))
    ax.scatter(posicoes, array, color="#141414")
    ax.errorbar(posicoes, array, desvio_padrao, linestyle='None', color="#141414")
    ax.set_ylabel("Valores", fontdict={"weight": "bold", "size": 14})
    ax.set_title("Carta de controle", fontdict={"weight": "bold", "size": 16})
    ax.axhline(li, color='#f2182a', linestyle='-', label='Limite Inferior')
    ax.axhline(ls, color='#f2182a', linestyle='-', label='Limite Superior')
    plt.savefig(caminho)
    plt.show()
    def filtrar():
        nonlocal array,li,ls
        valores_validos = array[np.where((array - desvio_padrao >= li)
                                         & (array + desvio_padrao <= ls))]
        valores_invalidos = array[np.where((array - desvio_padrao < li) |
                                           (array + desvio_padrao > ls))]
        return f'Valores válidos: {",".join(map(str, valores_validos))}\
               \nValores inválidos: {",".join(map(str, valores_invalidos))}'
    print(filtrar())

carta_controle(np.array([3.3, 2.7, 3.4, 2.8, 4, 3.7, 3.35, 4.2, 1.9]),Path(os.getcwd()) / "Carta_de_controle.png"\
,2,4)
