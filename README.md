<div style="text-align: justify">

# README - Projeto EEG_coffee_alert

## Introdução ao projeto

<div style="text-align: justify">
Bem-vindo ao projeto EEG_coffee_alert! Este é um repositório dedicado a um projeto de análise de dados EEG usando Python. Aqui você encontrará informações sobre a estrutura do repositório, detalhes sobre a base de dados utilizada e instruções para montar o ambiente virtual necessário para desenvolver e executar o projeto.
</div>

## Estrutura do repositório

<div style="text-align: right">
  <ul>
    <li><b>src</b>: Esta pasta contém os scripts Python responsáveis pelo processamento de dados EEG.</li>
    <li><b>environment.yml</b>: Arquivo YAML que permite a criação do ambiente virtual necessário para reproduzir o ambiente Anaconda utilizado no projeto.</li>
    <li><b>explorer.ipynb</b>: Notebook Jupyter que oferece uma interface para explorar os sinais EEG.</li>
    <li><b>requirements.txt</b>: Arquivo que lista os requisitos de software necessários para o projeto, como o google-cloud.</li>
  </ul>
</div>


## Detalhamento dos dados EEG

<div style="text-align: justify">
Os dados EEG utilizados neste projeto estão armazenados na pasta <b>/data</b>. Esses dados são fundamentais para as análises realizadas nos scripts Python presentes em <b>src</b> e no notebook <b>explorer.ipynb</b>.
</div>

## Montando o ambiente virtual

<div style="text-align: justify">
Este projeto utiliza a distribuição do <a href="https://www.anaconda.com/products/distribution">Anaconda</a> para criar o ambiente virtual em Python. No entanto, para uma instalação mais enxuta, recomendamos o uso do <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a>.
</div>

Para reproduzir o ambiente Python necessário para este projeto, execute o seguinte comando no terminal:

```bash
conda env create -f environment.yml
```

## Trabalhando com os dados no bucket
