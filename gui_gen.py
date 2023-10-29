from search_def import *
from graph_gen import *
from show_path import *
from graph_plot import *


def gerar_grafo():

    global entry_n_psdp, entry_n_psdp_desconto, entry_razao_desconto, entry_n_conexoes, mapa
    num_psdp = int(entry_n_psdp.get())
    num_psdp_desconto = int(entry_n_psdp_desconto.get())
    razao_desconto = float(entry_razao_desconto.get())
    num_conexoes = int(entry_n_conexoes.get())

    mapa = generate_rally_map(num_psdp, num_psdp_desconto, razao_desconto, num_conexoes)

    plota_sem_rota(mapa)

    gerar_livro_de_bordo()


def get_params_graph():

    global janela, entry_n_psdp, entry_n_psdp_desconto, entry_razao_desconto, entry_n_conexoes
    janela = tk.Tk()
    janela.title("Direção de Prova")

    label_n_psdp = tk.Label(janela, text="Número de PSDP:")
    label_n_psdp.grid(row=0, column=0, padx=5, pady=5)
    entry_n_psdp = tk.Entry(janela)
    entry_n_psdp.grid(row=0, column=1, padx=5, pady=5)

    label_n_psdp_desconto = tk.Label(janela, text="Número de PSDP com Desconto:")
    label_n_psdp_desconto.grid(row=1, column=0, padx=5, pady=5)
    entry_n_psdp_desconto = tk.Entry(janela)
    entry_n_psdp_desconto.grid(row=1, column=1, padx=5, pady=5)

    label_razao_desconto = tk.Label(janela, text="Razão de Desconto (de 0.0 até 1.0):")
    label_razao_desconto.grid(row=2, column=0, padx=5, pady=5)
    entry_razao_desconto = tk.Entry(janela)
    entry_razao_desconto.grid(row=2, column=1, padx=5, pady=5)

    label_n_conexoes = tk.Label(janela, text="Número de caminhos para cada PSDP:")
    label_n_conexoes.grid(row=3, column=0, padx=5, pady=5)
    entry_n_conexoes = tk.Entry(janela)
    entry_n_conexoes.grid(row=3, column=1, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela, text="Gerar Mapa", command=gerar_grafo)
    botao_gerar_grafo.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela, text="Abrir Menu do Road Book", command=gerar_livro_de_bordo)
    botao_gerar_grafo.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    janela.mainloop()


def gerar_livro_de_bordo():
    global entry_psdp_largada, entry_psdp_chegada
    # criar a janela do tkinter
    janela_livro_bordo = tk.Tk()
    janela_livro_bordo.title("Gerar Road Book")
    janela_livro_bordo.geometry("305x250")

    label_psdp_largada = tk.Label(janela_livro_bordo, text="PSDP de largada:")
    label_psdp_largada.grid(row=0, column=0, padx=5, pady=5)
    entry_psdp_largada = tk.Entry(janela_livro_bordo)
    entry_psdp_largada.grid(row=0, column=1, padx=5, pady=5)

    label_psdp_chegada = tk.Label(janela_livro_bordo, text="PSDP de chegada:")
    label_psdp_chegada.grid(row=1, column=0, padx=5, pady=5)
    entry_psdp_chegada = tk.Entry(janela_livro_bordo)
    entry_psdp_chegada.grid(row=1, column=1, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela_livro_bordo, text="Busca em largura", command=largura)
    botao_gerar_grafo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela_livro_bordo, text="Busca em profundidade", command=profundidade)
    botao_gerar_grafo.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela_livro_bordo, text="Busca gulosa", command=greedy_search_gui)
    botao_gerar_grafo.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    botao_gerar_grafo = tk.Button(janela_livro_bordo, text="Busca A*", command=a_start)
    botao_gerar_grafo.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    janela_livro_bordo.mainloop()


def largura():
    global mapa, entry_psdp_largada, entry_psdp_chegada

    psdp_largada = int(entry_psdp_largada.get())
    psdp_chegada = int(entry_psdp_chegada.get())

    rota_rapida = dfs(mapa, psdp_largada, psdp_chegada)

    navegador(mapa, rota_rapida)


def profundidade():
    global mapa, entry_psdp_largada, entry_psdp_chegada

    psdp_largada = int(entry_psdp_largada.get())
    psdp_chegada = int(entry_psdp_chegada.get())

    rota_rapida = bfs(mapa, psdp_largada, psdp_chegada)

    navegador(mapa, rota_rapida)


def greedy_search_gui():
    global mapa, entry_psdp_largada, entry_psdp_chegada

    psdp_largada = int(entry_psdp_largada.get())
    psdp_chegada = int(entry_psdp_chegada.get())

    rota_rapida, _ = greedy_search(mapa, psdp_largada, psdp_chegada)

    navegador(mapa, rota_rapida)


def a_start():
    global mapa, entry_psdp_largada, entry_psdp_chegada

    psdp_largada = int(entry_psdp_largada.get())
    psdp_chegada = int(entry_psdp_chegada.get())

    _, rota_rapida = astar_search(mapa, psdp_largada, psdp_chegada)

    navegador(mapa, rota_rapida)
