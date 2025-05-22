# Pipeline de Dados

Este projeto realiza o download, processamento e unificação de dados utilizando Python e Pandas.

## Estrutura

- `scripts/`: scripts de download e processamento.
- `data_raw/`: diretório onde são gravados arquivos originais após download feito na execução da Pipeline
- `data_processed/`: diretório onde são gravados arquivos após tratamento feito na execução da Pipeline

## Como executar

1. Clone o repositório.
2. Execute o script:
   - `executar_pipeline.py`
   Ao executá-lo, você estará realizando as ações dos seguintes arquivos:
   - `download_dados.py`
   - `processamento_dados.py`
   - `fusao_arquivos.py`

## Requisitos

- Python 3.10
- pandas
- requests
