from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_distribuicao_genero():
    # Consulta ao banco de dados para obter a distribuição dos atendimentos por sexo do consumidor
    cur = conn.cursor()
    cur.execute("SELECT CASE WHEN SexoConsumidor IN ('0', 'N') THEN 'Nao informado' ELSE SexoConsumidor END AS Sexo, COUNT(*) AS CountAtendimentos FROM Atendimento GROUP BY Sexo")
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    sexos = []
    contagem = []
    for row in data:
        sexos.append(row[0])
        contagem.append(row[1])

    # Criar o gráfico de pizza
    fig = go.Figure(data=go.Pie(labels=sexos, values=contagem))

    fig.update_layout(
        title='Distribuição dos Atendimentos por Gênero do Consumidor',
    )

    return fig.to_html()
