from weasyprint import HTML
from datetime import datetime

# Dados do relatório (simulação)
vendas = [
    {"produto": "Notebook Acer Aspire", "quantidade": 15, "preco_unitario": 3500.00},
    {"produto": "Mouse Óptico Logitech", "quantidade": 40, "preco_unitario": 85.00},
    {"produto": "Monitor Dell 24\"", "quantidade": 10, "preco_unitario": 850.00},
    {"produto": "Teclado Mecânico Redragon", "quantidade": 25, "preco_unitario": 200.00},
    {"produto": "Cabo HDMI 2.0 1.5m", "quantidade": 50, "preco_unitario": 25.00},
]

# Função para calcular o valor total de vendas
def calcular_total(vendas):
    return sum(item["quantidade"] * item["preco_unitario"] for item in vendas)

# Dados do relatório
total_vendas = calcular_total(vendas)
data_relatorio = datetime.now().strftime("%d/%m/%Y")

# Conteúdo HTML do relatório
html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Relatório de Vendas - Outubro 2024</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1, h2 {{
            text-align: center;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th, td {{
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        tfoot td {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Relatório de Vendas</h1>
    <h2>Outubro de 2024</h2>
    <p>Data de geração do relatório: {data_relatorio}</p>
    <table>
        <thead>
            <tr>
                <th>Produto</th>
                <th>Quantidade Vendida</th>
                <th>Preço Unitário (R$)</th>
                <th>Total (R$)</th>
            </tr>
        </thead>
        <tbody>
"""

# Adicionando as linhas da tabela com os dados de vendas
for item in vendas:
    total_item = item["quantidade"] * item["preco_unitario"]
    html_content += f"""
            <tr>
                <td>{item["produto"]}</td>
                <td>{item["quantidade"]}</td>
                <td>{item["preco_unitario"]:.2f}</td>
                <td>{total_item:.2f}</td>
            </tr>
    """

# Fechando o HTML com o total de vendas
html_content += f"""
        </tbody>
        <tfoot>
            <tr>
                <td colspan="3">Total Geral</td>
                <td>R$ {total_vendas:.2f}</td>
            </tr>
        </tfoot>
    </table>
</body>
</html>
"""

def gerar():
    nome = "relatorio_vendas_outubro_2024.pdf"
    HTML(string=html_content).write_pdf(nome)
    return nome

