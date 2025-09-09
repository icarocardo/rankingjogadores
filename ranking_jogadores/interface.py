import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# -------------------------------
# Conexão com o banco SQLite
# -------------------------------
def conectar():
    return sqlite3.connect("ranking.db")

def buscar_ranking():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, nivel, pontuacao FROM jogadores ORDER BY pontuacao DESC")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

# -------------------------------
# Interface Tkinter
# -------------------------------
root = tk.Tk()
root.title("🏆 Ranking de Jogadores 🏆")
root.geometry("600x400")

# Título
label = tk.Label(root, text="RANKING DE JOGADORES", font=("Arial", 16, "bold"))
label.pack(pady=10)

# Função para atualizar a tabela
def atualizar_tabela():
    for row in tree.get_children():
        tree.delete(row)
    ranking = buscar_ranking()
    for i, (nome, nivel, pontuacao) in enumerate(ranking, start=1):
        # Destaque para os 3 primeiros
        if i == 1:
            cor = "gold"
        elif i == 2:
            cor = "silver"
        elif i == 3:
            cor = "orange"
        else:
            cor = "white"
        tree.insert("", "end", values=(i, nome, nivel, f"{pontuacao:.2f}"), tags=(cor,))
    # Configura cores
    tree.tag_configure("gold", background="#FFD700")
    tree.tag_configure("silver", background="#C0C0C0")
    tree.tag_configure("orange", background="#CD7F32")
    tree.tag_configure("white", background="white")

# Botão atualizar
btn = tk.Button(root, text="Atualizar Ranking", command=atualizar_tabela, font=("Arial", 12))
btn.pack(pady=5)

# Tabela
columns = ("Posição", "Nome", "Nível", "Pontuação")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(expand=True, fill="both", padx=20, pady=10)

# Inicializa tabela
atualizar_tabela()

root.mainloop()