from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_variacao_tempo():
    # Consulta ao banco de dados para obter a variação dos atendimentos por região ou UF ao longo do tempo
    cur = conn.cursor()
    cur.execute('SELECT DataAtendimento, Regiao, COUNT(*) AS CountAtendimentos FROM Atendimento INNER JOIN Regiao ON Atendimento.CodigoRegiao = Regiao.CodigoRegiao GROUP BY DataAtendimento, Regiao ORDER BY DataAtendimento, Regiao')
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    datas = []
    regioes = []
    contagem = []
    for row in data:
        datas.append(row[0])
        regioes.append(row[1])
        contagem.append(row[2])

    # Criar o gráfico de linhas
    fig = go.Figure()
    for regiao in set(regioes):
        indices_regiao = [i for i, x in enumerate(regioes) if x == regiao]
        fig.add_trace(go.Scatter(x=[datas[i] for i in indices_regiao], y=[contagem[i]
                      for i in indices_regiao], mode='lines', name=str(regiao)))

    fig.update_layout(
        title='Variação dos Atendimentos por Região ou UF',
        xaxis=dict(title='Data de Atendimento'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
