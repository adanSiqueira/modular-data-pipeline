import pandas as pd
import requests
from pathlib import Path

def download_arquivo(url, destino):
    response = requests.get(url)
    with open(destino, 'wb') as f:
        f.write(response.content)
    print(f"✅ Download concluído: {destino}")

if __name__ == "__main__":
    # Diretório base: pasta 'pipeline_dados'
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_RAW_DIR = BASE_DIR / 'data_raw'
    DATA_RAW_DIR.mkdir(exist_ok=True)  # Cria a pasta se não existir

    # URLs dos arquivos
    urls = {
        'dados_empresaB.csv': 'https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaB.csv',
        'dados_empresaA.json': 'https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaA.json'
    }

    # Download de cada arquivo
    for nome_arquivo, url in urls.items():
        destino = DATA_RAW_DIR / nome_arquivo
        download_arquivo(url, destino)




