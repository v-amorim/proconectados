from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_principais_problemas_genero():
    # Consulta ao banco de dados para obter os principais problemas relatados por diferentes gêneros
    cur = conn.cursor()
    cur.execute("SELECT Problema.DescricaoProblema, Atendimento.SexoConsumidor, COUNT(*) AS CountProblemas FROM Atendimento INNER JOIN Problema ON Atendimento.CodigoProblema = Problema.CodigoProblema WHERE Atendimento.SexoConsumidor <> 'N' GROUP BY Problema.DescricaoProblema, Atendimento.SexoConsumidor ORDER BY CountProblemas DESC")
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    problemas = []
    generos = []
    contagem = []
    for row in data:
        problema = row[0].split('(')[0].strip()
        genero = row[1]
        count = row[2]

        if problema not in problemas:
            problemas.append(problema)
        if genero not in generos:
            generos.append(genero)

        contagem.append(count)

    # Ordenar os problemas por contagem decrescente
    problemas_ordenados = [problema for _, problema in sorted(zip(contagem, problemas), reverse=True)]
    problemas_5 = problemas_ordenados[:5]

    # Filtrar os dados apenas para os 5 problemas mais frequentes
    filtered_data = [row for row in data if row[0] in problemas_5]

    # Criar o gráfico de barras
    fig = go.Figure()

    for genero in generos:
        genero_contagem = [row[2] for row in filtered_data if row[1] == genero]
        fig.add_trace(go.Bar(x=problemas_5, y=genero_contagem, name=genero))

    fig.update_layout(
        title='Principais Problemas Relatados por Gênero',
        xaxis=dict(title='Problema'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
