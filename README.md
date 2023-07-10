<div  align="center">
	<a  href="https://www.alphaedtech.org.br/">
	<img  src="https://user-images.githubusercontent.com/79182711/187928980-1c1c834c-d92c-4565-b7b6-9cf5b644873e.png"  alt="Alpha EdTech"  title="Alpha EdTech"  width="250" />
	</a>
	<h1>
		Desafio Engenharia de Dados - [Proconectados](https://github.com/viniam/proconectados/tree/main)
		
	</h1>
</div>

### Requisitos do desafio

Neste desafio, proposto pelo programa Alpha EdTech, os grupos são criados pelos professores e deverá ser realizado os processos de "coleta", 'limpeza", "análise" e "visualização" de dados da **Administração Pública brasileira** tendo como requisitos:

- Uso das informações coletadas de um site da administração pública:
  - Uso da biblioteca `Pandas`;
  - Este processo poderá estático, isto é, a coleta pode ser feita em apenas uma etapa sem a necessidade de processamento dinâmico de informações;
  - A coleta normalmente será realizada processando-se um arquivo do tipo `CSV` por meio do uso do `Pandas`;
  - Deve-se realizar um tratamento para remover os dados não relevantes para o fim da aplicação ("limpeza").
  - Links de referências (não se restringindo a apenas estes):
    - [https://brasil.io/datasets/](https://brasil.io/datasets/)
    - [https://dados.gov.br/home](https://dados.gov.br/home)
- Uso de banco de dados relacional:
  - Uso do Postgres;
  - Mínimo de 5 tabelas;
  - As tabelas principais devem ter no mínimo 10 mil registros cada;
  - Não há a necessidade de uso de Spark, bastando o uso de Pandas;
  - Utilizar comandos SQL para o cruzamento das informações.
- Implementar e detalhar um processamento segmentado em no mínimo 3 zonas:
  - _raw_ (dado cru);
  - _curated_ (dado limpo); e
  - _analytics_ (dado analisado).
- Montagem do _data warehouse_ com as informações das tabelas:
  - Devem utilizar algoritmos que demonstram a habilidade em estrutura de dados e complexidade de algoritmos.
- Visualização dos dados analisados usando `Flask`;
- Uso da análise estatística dos dados usando `Plotly`:
  - Uso de estatística básica;
  - Não é necessário o uso de regressões.

## Objetivo

O tema escolhido foi o de explorar as informações coletadas do site do ministério da justiça em relação aos atendimentos do Procon, para análise de dados.

## Tecnologias

#### **Dependências**

- **[Python](https://docs.python.org/pt-br/3/tutorial/index.html)**
- **[Pip-tools](https://github.com/jazzband/pip-tools)**
- **[Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)**
- **[PostgreSQL](https://www.postgresql.org/)**
- **[Plotly](https://plotly.com/python/)**
- **[Flask](https://flask.palletsprojects.com/en/2.3.x/)**

## Referências

- [Fonte dos Dados do Procon](https://dados.mj.gov.br/dataset/atendimentos-de-consumidores-nos-procons-sindec)
- [Apresentação do Projeto](https://www.canva.com/design/DAFn6ie8Hts/Wvi_IWp69N8Jvp6jkI2S9w/view?utm_content=DAFn6ie8Hts&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
- [Setup para poder executar](https://github.com/viniam/proconectados/blob/main/SETUP.md)

## Licença

Esse repositório está licenciado pela **Mit License**. Para mais informações detalhadas, leia o arquivo [License](https://github.com/viniam/proconectados/blob/main/LICENSE) contido nesse repositório.

## Equipe

<table align="center">
	<tr>
		<td align="center">
			<a href="https://github.com/viniam"><img src="https://avatars.githubusercontent.com/u/629036?v=4" width="100px;" alt="Vinicius Amorim"/><br /><sub><b>Vinicius Amorim</b></sub></a><br />🚀<br />
		</td>
		<td align="center">
			<a href="https://github.com/geversonfernandes"><img src="https://avatars.githubusercontent.com/u/31553941?v=4" width="100px;" alt="Geverson Araujo Fernandes"/><br /><sub><b>Geverson Araujo Fernandes</b></sub></a><br />🚀<br />
        </td>
	</tr>
</table>
