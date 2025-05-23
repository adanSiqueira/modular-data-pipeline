# Pipeline de Processamento e Unificação de Dados

Este projeto consiste em uma **pipeline automatizada** que realiza o download, carregamento, transformação e unificação de dados provenientes de arquivos `JSON` e `CSV`. Ao final do processo, os dados tratados e padronizados são armazenados em um único arquivo `CSV`, pronto para análise ou integração em outros sistemas.

## Principais Funcionalidades

✅ Download automático de arquivos a partir de URLs  
✅ Estrutura modular e organizada em scripts independentes  
✅ Transformação de dados: renomeação e padronização de colunas  
✅ Unificação de múltiplas fontes de dados em um único dataset  
✅ Armazenamento seguro e organizado dos arquivos brutos e processados  

## Estrutura do Projeto
```
pipeline_dados/
├── data_processed/ # Arquivo final, tratado e unificado
├── data_raw/ # Arquivos brutos, baixados da internet
├── notebooks/ # Notebook exploratório inicial
├── scripts/ # Scripts principais da pipeline
│ ├── download_dados.py # Realiza o download automatizado dos arquivos
│ ├── processamento_dados.py # Classe com métodos para carregar, transformar e salvar os dados
│ ├── fusao_arquivos.py # Script que executa a fusão dos arquivos
│ └── executar_pipeline.py # Script que executa toda a pipeline de ponta a ponta
└── README.md # Documentação do projeto
```


##  Como Funciona a Pipeline

1. **Download**: baixa automaticamente os arquivos JSON e CSV a partir de links públicos, salvando-os na pasta `data_raw`.
2. **Carregamento**: lê os arquivos baixados para o ambiente de processamento.
3. **Transformação**: padroniza nomes de colunas, garantindo consistência entre os datasets.
4. **Unificação**: concatena os dados, preenchendo eventuais informações ausentes.
5. **Exportação**: salva o resultado final na pasta `data_processed`.

## Scripts e Classes

### `download_dados.py`
Realiza o download dos arquivos a partir de URLs, armazenando-os automaticamente na pasta `data_raw`.

### `processamento_dados.py`
Contém a classe `Dados` com métodos encadeados que executam toda a pipeline: carregar, transformar, unificar e salvar.

### `fusao_arquivos.py`
Script que instancia a classe `Dados` e executa a pipeline de forma direta, após o download manual dos arquivos.

### `executar_pipeline.py`
Script completo que **baixa os arquivos** e **executa a pipeline** automaticamente de ponta a ponta, ideal para processos automatizados.

## Exemplo de Execução

Para rodar a pipeline completa, basta executar:

```bash
python scripts/executar_pipeline.py
```

Ao final, o arquivo dados_unificados.csv estará disponível na pasta data_processed.

## Por que este projeto é interessante?
**Automação**: do download ao processamento, tudo pode ser executado com um único comando.

**Reusabilidade**: a classe Dados pode ser aplicada a outros projetos que exijam processos similares.

**Organização**: os dados brutos e processados são armazenados em pastas distintas, seguindo boas práticas de engenharia de dados.

## Exploração dos Dados
Na pasta notebooks há um notebook exploratório, onde foram realizadas análises iniciais para entender a estrutura dos dados e definir as transformações necessárias.

## Requisitos

- Python 3.10
- pandas
- requests
