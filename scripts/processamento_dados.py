import pandas as pd
from pathlib import Path

class Dados:
    def __init__(self, path_json, path_csv, output_path='dados_unificados.csv'):
        self.path_json = Path(path_json).resolve()
        self.path_csv = Path(path_csv).resolve()
        self.output_path = Path(output_path).resolve()
        self.dados_unificados = None

    def carregar(self):
        self.dados_json = pd.read_json(self.path_json)
        self.dados_csv = pd.read_csv(self.path_csv)
        return self

    def transformar(self):
        mapeamento_colunas = {
            'Nome do Item': 'Nome do Produto',
            'Classificação do Produto': 'Categoria do Produto',
            'Valor em Reais (R$)': 'Preço do Produto (R$)',
            'Nome da Loja': 'Filial'
        }
        self.dados_csv = self.dados_csv.rename(columns=mapeamento_colunas)
        return self

    def unificar(self):
        self.dados_unificados = pd.concat(
            [self.dados_json, self.dados_csv], ignore_index=True
        )
        self.dados_unificados['Data da Venda'] = self.dados_unificados['Data da Venda'].fillna(
            'Informação não disponível'
        )
        return self

    def salvar(self):
        self.dados_unificados.to_csv(self.output_path, index=False)
        return self

    def executar_pipeline(self):
        return self.carregar().transformar().unificar().salvar()
