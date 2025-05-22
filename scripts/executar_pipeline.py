from pathlib import Path
from download_dados import download_arquivo
from processamento_dados import Dados

if __name__ == "__main__":
    # Diretório base
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_RAW_DIR = BASE_DIR / 'data_raw'
    DATA_PROCESSED_DIR = BASE_DIR / 'data_processed'

    # Garante que as pastas existam
    DATA_RAW_DIR.mkdir(exist_ok=True)
    DATA_PROCESSED_DIR.mkdir(exist_ok=True)

    # URLs dos arquivos
    urls = {
        'dados_empresaB.csv': 'https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaB.csv',
        'dados_empresaA.json': 'https://raw.githubusercontent.com/alura-cursos/Pipeline-de-dados-combinando-Python-e-orientcao-a-objeto/main/data_raw/dados_empresaA.json'
    }

    # Download de cada arquivo
    for nome_arquivo, url in urls.items():
        destino = DATA_RAW_DIR / nome_arquivo
        download_arquivo(url, destino)

    # Executa a pipeline de processamento
    path_json = DATA_RAW_DIR / 'dados_empresaA.json'
    path_csv = DATA_RAW_DIR / 'dados_empresaB.csv'
    output_path = DATA_PROCESSED_DIR / 'dados_unificados.csv'

    dados = Dados(path_json, path_csv, output_path)
    dados.executar_pipeline()

    print(f"Pipeline concluída! Arquivo salvo em: {output_path}")
