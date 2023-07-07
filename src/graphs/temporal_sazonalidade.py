from __future__ import annotations

import random

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_sazonalidade():
    # Consulta ao banco de dados para obter os dados de sazonalidade
    cur = conn.cursor()
    cur.execute('SELECT AnoAtendimento, MesAtendimento, COUNT(*) AS CountAtendimentos FROM Atendimento GROUP BY AnoAtendimento, MesAtendimento ORDER BY AnoAtendimento, MesAtendimento')
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    anos = []
    meses = []
    contagem = []
    for row in data:
        anos.append(row[0])
        meses.append(row[1])
        contagem.append(row[2])

    # Definir as cores para cada ano
    cores = ['rgb(239, 85, 59)', 'rgb(99, 110, 250)']

    # Criar o gráfico de retas com cores diferentes para cada ano
    fig = go.Figure()
    for i, ano in enumerate(set(anos)):
        indices_ano = [i for i, x in enumerate(anos) if x == ano]
        cor = cores[i % len(cores)]
        fig.add_trace(go.Scatter(x=[meses[i] for i in indices_ano], y=[contagem[i]
                      for i in indices_ano], mode='lines', name=str(ano), line=dict(color=cor)))

    fig.update_layout(
        title='Sazonalidade de Atendimentos',
        xaxis=dict(title='Mês'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
