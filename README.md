# Data Processing and Unification Pipeline

This project consists of an **automated pipeline** that downloads, loads, transforms, and unifies data from `JSON` and `CSV` files. At the end of the process, the cleaned and standardized data is stored in a single `CSV` file, ready for analysis or integration into other systems.

## Main Features

✅ Automatic file download from URLs  
✅ Modular structure organized into independent scripts  
✅ Data transformation: column renaming and standardization  
✅ Unification of multiple data sources into a single dataset  
✅ Secure and organized storage of raw and processed files  

## Project Structure

```
data_pipeline/
├── data_processed/ # Final, cleaned and unified file
├── data_raw/ # Raw files downloaded from the internet
├── notebooks/ # Initial exploratory notebook
├── scripts/ # Main pipeline scripts
│ ├── download_dados.py # Automates file download
│ ├── processamento_dados.py # Class with methods to load, transform, and save data
│ ├── fusao_arquivos.py # Script to merge files
│ └── executar_pipeline.py # Script to execute the full end-to-end pipeline
└── README.md # Project documentation
```

## How the Pipeline Works

1. **Download**: Automatically downloads JSON and CSV files from public URLs, saving them in the `data_raw` folder.  
2. **Loading**: Reads the downloaded files into the processing environment.  
3. **Transformation**: Standardizes column names to ensure consistency across datasets.  
4. **Unification**: Concatenates the data, filling in any missing information.  
5. **Export**: Saves the final result in the `data_processed` folder.

## Scripts and Classes

### `download_dados.py`
Downloads files from URLs and automatically stores them in the `data_raw` folder.

### `processamento_dados.py`
Contains the `Dados` class with chained methods to execute the entire pipeline: load, transform, unify, and save.

### `fusao_arquivos.py`
Script that instantiates the `Dados` class and directly runs the pipeline after manual file download.

### `executar_pipeline.py`
Complete script that **downloads files** and **runs the pipeline** end to end — ideal for automated processes.

## Execution Example

To run the full pipeline, simply execute:

```bash
python scripts/executar_pipeline.py
```

At the end, the dados_unificados.csv file will be available in the data_processed folder.

## Why Is This Project Interesting?
**Automation**: From download to processing, everything can be executed with a single command.

**Reusability**: The Dados class can be reused in other projects that require similar processing steps.

**Organization**: Raw and processed data are stored in separate folders, following best practices in data engineering.

## Exploring Data
Inside the notebooks folder, there is an exploratory notebook where initial analyses were conducted to understand the data structure and define the necessary transformations.

## Requirements

- Python 3.10
- pandas
- requests
