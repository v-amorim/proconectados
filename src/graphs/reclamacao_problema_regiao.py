from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_destaques_regiao_uf(uf_regiao=None):
    # Consulta ao banco de dados para verificar os assuntos e problemas que se destacam em determinadas regiões ou UF
    cur = conn.cursor()
    query = 'SELECT Regiao, UF, Assunto.DescricaoAssunto, Problema.DescricaoProblema, COUNT(*) AS Contagem FROM Atendimento INNER JOIN Regiao ON Atendimento.CodigoRegiao = Regiao.CodigoRegiao INNER JOIN Assunto ON Atendimento.CodigoAssunto = Assunto.CodigoAssunto INNER JOIN Problema ON Atendimento.CodigoProblema = Problema.CodigoProblema'
    if uf_regiao:
        query += f" WHERE Regiao = '{uf_regiao}' OR UF = '{uf_regiao}'"
    query += ' GROUP BY Regiao, UF, Assunto.DescricaoAssunto, Problema.DescricaoProblema ORDER BY Contagem DESC'

    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    regioes_uf = []
    assuntos = []
    contagem = []
    for row in data:
        regiao_uf = f'{row[0]} - {row[1]}'
        assuntos.append(row[2])
        contagem.append(row[4])
        regioes_uf.append(regiao_uf)

    # Criar o gráfico de barras
    fig = go.Figure(data=go.Bar(x=regioes_uf, y=contagem))

    fig.update_layout(
        title='Destaques por Região ou UF',
        xaxis=dict(title='Região ou UF'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
