from __future__ import annotations

from database.database_config import create_connection
from flask import Flask
from flask import render_template
from flask import request
from graphs.demografica_faixa_etaria_atendimento import obter_dados_distribuicao_faixa_etaria
from graphs.demografica_faixa_etaria_problema import obter_dados_principais_problemas_faixa_etaria
from graphs.demografica_genero_atendimento import obter_dados_distribuicao_genero
from graphs.demografica_genero_problema import obter_dados_principais_problemas_genero
from graphs.geografica_regiao_distribuicao import obter_dados_distribuicao_regiao
from graphs.geografica_regiao_variacao import obter_dados_variacao_tempo
from graphs.reclamacao_assuntos import obter_dados_assuntos_recorrentes
from graphs.reclamacao_problema_comum import obter_dados_problemas_comuns
from graphs.reclamacao_problema_regiao import obter_dados_destaques_regiao_uf
from graphs.temporal_sazonalidade import obter_dados_sazonalidade
from graphs.temporal_tendencias import obter_dados_tendencias

# Conectar ao banco de dados PostgreSQL
conn = create_connection()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/temporal_tendencias')
def temporal_tendencias():
    plot = obter_dados_tendencias()
    return render_template('temporal_tendencias.html', plot=plot)


@app.route('/temporal_sazonalidade')
def temporal_sazonalidade():
    plot = obter_dados_sazonalidade()
    return render_template('temporal_sazonalidade.html', plot=plot)


@app.route('/geografica_regiao_distribuicao')
def geografica_regiao_distribuicao():
    plot = obter_dados_distribuicao_regiao()
    return render_template('geografica_regiao_distribuicao.html', plot=plot)


@app.route('/geografica_regiao_variacao')
def geografica_regiao_variacao():
    plot = obter_dados_variacao_tempo()
    return render_template('geografica_regiao_variacao.html', plot=plot)


@app.route('/reclamacao_assuntos')
def reclamacao_assuntos():
    ano_selecionado = request.args.get('ano')
    plot = obter_dados_assuntos_recorrentes(ano_selecionado)
    return render_template('reclamacao_assuntos.html', plot=plot)


@app.route('/reclamacao_problema_comum')
def reclamacao_problema_comum():
    ano_selecionado = request.args.get('ano')
    plot = obter_dados_problemas_comuns(ano_selecionado)
    return render_template('reclamacao_problema_comum.html', plot=plot)


@app.route('/reclamacao_problema_regiao')
def reclamacao_problema_regiao():
    uf_regiao = request.args.get('uf_regiao')
    plot = obter_dados_destaques_regiao_uf(uf_regiao)
    return render_template('reclamacao_problema_regiao.html', plot=plot)


@app.route('/demografica_genero_atendimento')
def demografica_genero_atendimento():
    plot = obter_dados_distribuicao_genero()
    return render_template('demografica_genero_atendimento.html', plot=plot)


@app.route('/demografica_faixa_etaria_atendimento')
def demografica_faixa_etaria_atendimento():
    plot = obter_dados_distribuicao_faixa_etaria()
    return render_template('demografica_faixa_etaria_atendimento.html', plot=plot)


@app.route('/demografica_genero_problema')
def demografica_genero_problema():
    plot = obter_dados_principais_problemas_genero()
    return render_template('demografica_genero_problema.html', plot=plot)


@app.route('/demografica_faixa_etaria_problema')
def demografica_faixa_etaria_problema():
    plot = obter_dados_principais_problemas_faixa_etaria()
    return render_template('demografica_faixa_etaria_problema.html', plot=plot)


if __name__ == '__main__':
    app.run(debug=True)
