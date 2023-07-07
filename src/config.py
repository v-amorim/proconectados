from __future__ import annotations

csv_encodings = ['utf-8', 'cp1252']
csv_separators = [';', '\t']

dataset_source_url = 'https://dados.mj.gov.br/dataset/atendimentos-de-consumidores-nos-procons-sindec'
dataset_folder_name = 'csv_files'
dataset_ignore_list = ['fornecedor']
dataset_years = [2019, 2020]

# key: column name
# value: tuple(data type, slice size)
dataset_value_dictionary = {
    'AnoAtendimento': ('int64', None),
    'TrimestreAtendimento': ('int64', None),
    'MesAtendimento': ('int64', None),
    'DataAtendimento': ('datetime64[ns]', None),
    'CodigoRegiao': ('object', 2),
    'Regiao': ('object', 15),
    'UF': ('object', 2),
    'CodigoTipoAtendimento': ('int64', None),
    'DescricaoTipoAtendimento': ('object', 50),
    'CodigoAssunto': ('int64', None),
    'DescricaoAssunto': ('object', 160),
    'GrupoAssunto': ('object', 160),
    'CodigoProblema': ('int64', None),
    'DescricaoProblema': ('object', 160),
    'GrupoProblema': ('object', 160),
    'SexoConsumidor': ('object', 1),
    'FaixaEtariaConsumidor': ('object', 20),
    'CEPConsumidor': ('object', 8)
}
