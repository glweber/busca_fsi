import tkinter as tk

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plota_sem_rota(graph: nx.Graph):
    fig, ax = plt.subplots(figsize=(30, 30))

    pos = nx.spring_layout(graph, k=0.9)
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

    for node in graph.nodes():
        if 'time_discount' in graph.nodes[node] and graph.nodes[node]['time_discount'] > 0:
            plt.text(pos[node][0], pos[node][1] + 0.05, f"{graph.nodes[node]['time_discount']:.2f}", fontsize=10,
                     ha="center", bbox=dict(facecolor='white', alpha=0.7))

    # criar a janela do tkinter
    root = tk.Tk()
    root.title("Rally Map")
    root.geometry("1000x1000")

    # criar o canvas do matplotlib e adicionar à janela do tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # adicionar um botão para fechar a janela
    button = tk.Button(root, text="Fechar", command=root.quit)
    button.pack()

    # iniciar o loop do tkinter
    tk.mainloop()
