<div style="text-align: justify">

# README - Projeto EEG_coffee_alert

## Introdução ao projeto


Bem-vindo ao projeto EEG_coffee_alert! Este é um repositório dedicado a um projeto de análise de dados EEG usando Python. Aqui você encontrará informações sobre a estrutura do repositório, detalhes sobre a base de dados utilizada e instruções para montar o ambiente virtual necessário para desenvolver e executar o projeto.

## Estrutura do repositório

- **src**: Esta pasta contém os scripts Python responsáveis pelo processamento de dados EEG.
- **environment.yml**: Arquivo YAML que permite a criação do ambiente virtual necessário para reproduzir o ambiente Anaconda utilizado no projeto.
- **explorer.ipynb**: Notebook Jupyter que oferece uma interface para explorar os sinais EEG.
- **requirements.txt**: Arquivo que lista os requisitos de software necessários para o projeto, como o google-cloud.

## Detalhamento dos dados EEG

Os dados EEG utilizados neste projeto estão armazenados na pasta **/data**. Esses dados são fundamentais para as análises realizadas nos scripts Python presentes em **src** e no notebook **explorer.ipynb**.

## Montando o ambiente virtual

Este projeto utiliza a distribuição do [Anaconda](https://www.anaconda.com/products/distribution) para criar o ambiente virtual em Python. No entanto, para uma instalação mais enxuta, recomendamos o uso do [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Para reproduzir o ambiente Python necessário para este projeto, execute o seguinte comando no terminal:

```bash <center>
conda env create -f environment.yml
```

## Trabalhando com os dados no bucket
