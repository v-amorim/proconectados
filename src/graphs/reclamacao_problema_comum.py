from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_problemas_comuns(ano_selecionado=None):
    # Consulta ao banco de dados para obter os problemas mais comuns relatados pelos consumidores
    cur = conn.cursor()
    query = 'SELECT Problema.DescricaoProblema, COUNT(*) AS CountProblemas FROM Atendimento INNER JOIN Problema ON Atendimento.CodigoProblema = Problema.CodigoProblema'
    if ano_selecionado:
        query += f' WHERE EXTRACT(YEAR FROM Atendimento.DataAtendimento) = {ano_selecionado}'
    query += ' GROUP BY Problema.DescricaoProblema ORDER BY CountProblemas DESC LIMIT 5'

    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    problemas = []
    contagem = []
    for row in data:
        problema = row[0].split('(')[0].strip()
        problemas.append(problema)
        contagem.append(row[1])

    # Criar o gráfico de barras
    fig = go.Figure(data=go.Bar(x=problemas, y=contagem))

    fig.update_layout(
        title='Problemas Mais Comuns Relatados pelos Consumidores',
        xaxis=dict(title='Problema'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
