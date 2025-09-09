import csv

def ler_csv(arquivo_csv, log_erros="erros.log"):
    jogadores = []
    with open(arquivo_csv, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            try:
                nome = linha["nome"]
                nivel = int(linha["nivel"])
                pontuacao = float(linha["pontuacao"])
                jogadores.append((nome, nivel, pontuacao))
            except Exception as e:
                with open(log_erros, "a", encoding="utf-8") as log:
                    log.write(f"Erro na linha {linha}: {e}\n")
    return jogadores




