import pandas as pd

# Lê o CSV e converte para uma lista de dicionários
users = pd.read_csv(r"C:\Users\dindi\OneDrive\Área de Trabalho\dados_pandas_antes.csv").to_dict(orient="records")
mensagem_opcoes = pd.read_csv(r"C:\Users\dindi\OneDrive\Área de Trabalho\dados_opcoes.csv").to_dict(orient="records")

# Avalia o saldo de cada usuário e atribui a mensagem correspondente
for user in users:
    if user["conta_saldo"] < 50:
        mensagem = mensagem_opcoes[0]["mensagem"]
    elif user["conta_saldo"] <= 500:
        mensagem = mensagem_opcoes[1]["mensagem"]
    else:
        mensagem = (mensagem_opcoes[2]["mensagem"]).strip("\"")
    user["mensagem"] = mensagem
    print(f"{user["nome"]}: {user["mensagem"]}\n")

# Salva o DataFrame atualizado em um novo arquivo CSV
users_df = pd.DataFrame(users)         
users_df.to_csv(r"C:\Users\dindi\OneDrive\Área de Trabalho\dados_pandas_depois.csv", index=False, encoding='utf-8')
print(f"\nArquivo 'dados_pandas_depois.csv' criado com sucesso!")