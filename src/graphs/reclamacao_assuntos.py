from __future__ import annotations

import plotly.graph_objects as go
from database.database_config import create_connection

# Conectar ao banco de dados PostgreSQL
conn = create_connection()


def obter_dados_assuntos_recorrentes(ano_selecionado=None):
    # Consulta ao banco de dados para obter os assuntos mais recorrentes nas reclamações
    cur = conn.cursor()
    query = 'SELECT Assunto.DescricaoAssunto, COUNT(*) AS CountReclamacoes FROM Atendimento INNER JOIN Assunto ON Atendimento.CodigoAssunto = Assunto.CodigoAssunto'
    if ano_selecionado:
        query += f' WHERE EXTRACT(YEAR FROM Atendimento.DataAtendimento) = {ano_selecionado}'
    query += ' GROUP BY Assunto.DescricaoAssunto ORDER BY CountReclamacoes DESC LIMIT 5'

    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    # Processar os dados
    assuntos = []
    contagem = []
    for row in data:
        assunto = row[0].split('(')[0].strip()
        assuntos.append(assunto)
        contagem.append(row[1])

    # Criar o gráfico de barras
    fig = go.Figure(data=go.Bar(x=assuntos, y=contagem))

    fig.update_layout(
        title='Assuntos Mais Recorrentes nas Reclamações',
        xaxis=dict(title='Assunto'),
        yaxis=dict(title='Contagem')
    )

    return fig.to_html()
