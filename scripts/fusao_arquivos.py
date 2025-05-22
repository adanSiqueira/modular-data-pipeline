from processamento_dados import Dados
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # sobe da pasta scripts para pipeline_dados

path_json = BASE_DIR / 'data_raw' / 'dados_empresaA.json'
path_csv = BASE_DIR / 'data_raw' / 'dados_empresaB.csv'
output_path = BASE_DIR / 'data_processed' / 'dados_unificados.csv'

dados = Dados(path_json, path_csv, output_path)
dados.executar_pipeline()
