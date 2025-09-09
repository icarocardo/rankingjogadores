import sqlite3

def conectar():
    return sqlite3.connect("ranking.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nivel INTEGER NOT NULL,
            pontuacao REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()