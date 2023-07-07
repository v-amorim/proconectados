from __future__ import annotations

import random

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_tendencias():
    # Consulta ao banco de dados para obter os dados de tendências
    cur = conn.cursor()
    cur.execute('SELECT AnoAtendimento, TrimestreAtendimento, MesAtendimento, COUNT(*) AS CountAtendimentos FROM Atendimento GROUP BY AnoAtendimento, TrimestreAtendimento, MesAtendimento ORDER BY AnoAtendimento, TrimestreAtendimento, MesAtendimento')
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    anos = []
    trimestres = []
    meses = []
    contagem = []
    for row in data:
        anos.append(row[0])
        trimestres.append(row[1])
        meses.append(row[2])
        contagem.append(row[3])

    # Definir as cores para cada ano
    cores = ['rgb(239, 85, 59)', 'rgb(99, 110, 250)']  # Cores especificadas

    # Criar o gráfico de barras verticais com cores diferentes para cada ano
    fig = go.Figure()
    for i, ano in enumerate(set(anos)):
        indices_ano = [j for j, x in enumerate(anos) if x == ano]
        cor = cores[i % len(cores)]
        fig.add_trace(go.Bar(x=[meses[j] for j in indices_ano], y=[contagem[j]
                      for j in indices_ano], name=str(ano), marker=dict(color=cor)))

    fig.update_layout(
        title='Tendências de Atendimentos',
        xaxis=dict(title='Mês'),
        yaxis=dict(title='Contagem'),
        barmode='group'
    )

    return fig.to_html()
