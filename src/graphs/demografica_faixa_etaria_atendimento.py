from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_distribuicao_faixa_etaria():
    # Consulta ao banco de dados para obter a distribuição dos atendimentos por faixa etária do consumidor
    cur = conn.cursor()
    cur.execute("SELECT FaixaEtariaConsumidor, COUNT(*) AS CountAtendimentos FROM Atendimento GROUP BY FaixaEtariaConsumidor ORDER BY CASE FaixaEtariaConsumidor WHEN 'até 20 anos' THEN 1 WHEN 'entre 21 a 30 anos' THEN 2 WHEN 'entre 31 a 40 anos' THEN 3 WHEN 'entre 41 a 50 anos' THEN 4 WHEN 'entre 51 a 60 anos' THEN 5 WHEN 'entre 61 a 70 anos' THEN 6 WHEN 'mais de 70 anos' THEN 7 WHEN 'Nao Informada' THEN 8 WHEN 'Nao se aplica' THEN 9 ELSE 10 END")
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    faixas_etarias = []
    contagem = []
    for row in data:
        faixas_etarias.append(row[0])
        contagem.append(row[1])

    # Criar o gráfico de pizza
    fig = go.Figure(data=go.Pie(labels=faixas_etarias, values=contagem))

    fig.update_layout(
        title='Distribuição dos Atendimentos por Faixa Etária do Consumidor',
    )

    fig.update_traces(sort=False)

    return fig.to_html()
