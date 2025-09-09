from database import criar_tabela, conectar
from utils import ler_csv

def importar_csv(arquivo_csv):
    jogadores = ler_csv(arquivo_csv)
    conn = conectar()
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO jogadores (nome, nivel, pontuacao) VALUES (?, ?, ?)", jogadores)
    conn.commit()
    conn.close()
    print(f"{len(jogadores)} jogadores importados!")

def exibir_ranking():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, nivel, pontuacao FROM jogadores ORDER BY pontuacao DESC")
    jogadores = cursor.fetchall()
    conn.close()

    print("\n🏆 RANKING DOS JOGADORES 🏆")
    for i, (nome, nivel, pontuacao) in enumerate(jogadores, start=1):
        destaque = "⭐" if i <= 3 else ""
        print(f"{i}. {nome} (Nível {nivel}) - {pontuacao:.2f} {destaque}")

if __name__ == "__main__":
    criar_tabela()
    importar_csv("jogadores.csv")
    exibir_ranking()



