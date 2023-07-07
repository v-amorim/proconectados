from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_distribuicao_regiao():
    # Consulta ao banco de dados para obter a distribuição dos atendimentos por região
    cur = conn.cursor()
    cur.execute('SELECT Regiao, COUNT(*) AS CountAtendimentos FROM Atendimento INNER JOIN Regiao ON Atendimento.CodigoRegiao = Regiao.CodigoRegiao GROUP BY Regiao ORDER BY Regiao')
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    regioes = []
    contagem = []
    for row in data:
        regioes.append(row[0])
        contagem.append(row[1])

    # Criar o gráfico de pizza
    fig = go.Figure(data=go.Pie(labels=regioes, values=contagem))

    return fig.to_html()
