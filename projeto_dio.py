import pandas as pd

# Cria DataFrames (tabelas)
dados_df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "nome": ["Miete", "Tigrao", "Popcorn", "Chuzzlewit", "Amor", "Kitty", "Fuba", "Lucci", "Romeo", "Tom", "Sherockinho", "Chopin", "Nocturnes"],
    "Conta_numero": ["48291-3", "10942-8", "77301-5", "23940-0", "88127-2", "55631-9", "12098-4", "93422-7", "30511-6", "68293-1", "41720-8", "19283-5", "84056-2"],
    "Conta_agencia": ["1042", "3391", "7205", "1184", "9023", "4457", "6612", "2839", "5504", "8871", "3019", "4928", "7740"],
    "conta_saldo": [150.50, 1240.00, 45.90, 8920.15, 310.00, 15780.40, 2350.65, 99.00, 412.33, 6700.00, 12.50, 3450.20, 820.75],
    "conta_limite": [500.00, 1200.00, 3500.00, 100.00, 8000.00, 2500.00, 15000.00, 450.00, 6200.00, 1000.00, 300.00, 12500.00, 2100.00],    
})

opcoes_df = pd.DataFrame({
    "opcao_id": [1, 2, 3],
    "mensagem": [
        "Seu saldo está baixo, considere fazer um depósito.",
        "Parabéns! Você tem um saldo saudável.",
        "Considere investir seu dinheiro para melhores rendimentos."
    ]
})

# Salva os DataFrames em arquivos CSV
dados_df.to_csv(r"C:\Users\dindi\OneDrive\Área de Trabalho\dados_pandas_antes.csv", index=False, encoding='utf-8')
print("Arquivo 'dados_pandas_antes.csv' criado com sucesso!")

opcoes_df.to_csv(r"C:\Users\dindi\OneDrive\Área de Trabalho\dados_opcoes.csv", index=False, encoding='utf-8')  
print("Arquivo 'dados_opcoes.csv' criado com sucesso!")

