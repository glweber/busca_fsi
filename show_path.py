import tkinter as tk
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def navegador(graph: nx.Graph, caminho_otimo: List[int], wait_time: float = 0):
    fig, ax = plt.subplots(figsize=(30, 30))

    pos = nx.spring_layout(graph, k=1.5)
    node_sizes = [500 if 'time_discount' in graph.nodes[node] and graph.nodes[node]['time_discount'] > 0 else 200 for
                  node in graph.nodes()]
    node_colors = [
        'orange' if 'time_discount' in graph.nodes[node] and graph.nodes[node]['time_discount'] > 0 else 'lightblue' for
        node in graph.nodes()]

    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=node_sizes, ax=ax)
    nx.draw_networkx_labels(graph, pos, ax=ax)

    edges = list(graph.edges())
    edge_labels = {(u, v): f"{graph[u][v]['cost']:.2f}" for u, v in edges}

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)
    nx.draw_networkx_edges(graph, pos, edgelist=edges, alpha=0.5, ax=ax)

    path = [(caminho_otimo[i], caminho_otimo[i + 1]) for i in range(len(caminho_otimo) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=path, edge_color='red', ax=ax,
                           width=2.0)  # destaca o caminho ótimo com largura de 2

    custo_total = sum([graph[u][v]['cost'] for u, v in path])
    caminho = " -> ".join([str(node) for node in caminho_otimo])
    info_text = f'Caminho ideal: {caminho}\nCusto total: {custo_total:.2f}'
    plt.gcf().text(0.05, 0.05, info_text, fontsize=15)

    for node in graph.nodes():
        if 'time_discount' in graph.nodes[node] and graph.nodes[node]['time_discount'] > 0:
            plt.text(pos[node][0], pos[node][1] + 0.05, f"{graph.nodes[node]['time_discount']:.2f}", fontsize=10,
                     ha="center", bbox=dict(facecolor='white', alpha=0.7))

    # criar a janela do tkinter
    janela_navegador = tk.Tk()
    janela_navegador.title("Mapa")
    janela_navegador.geometry("1000x1000")

    # criar o canvas do matplotlib e adicionar à janela do tkinter
    canvas = FigureCanvasTkAgg(fig, master=janela_navegador)
    canvas.draw()
    canvas.get_tk_widget().pack()

    button = tk.Button(janela_navegador, text="Fechar", command=janela_navegador.quit)
    button.pack()

    tk.mainloop()
