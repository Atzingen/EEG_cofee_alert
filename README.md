<h1>README - Projeto EEG_coffee_alert</h1>

<div align="justify">
<h2>Introdução ao projeto</h2>
<p>
Bem-vindo ao projeto EEG_coffee_alert! Este é um repositório dedicado a um projeto de análise de dados EEG usando Python. Aqui você encontrará informações sobre a estrutura do repositório, detalhes sobre a base de dados utilizada e instruções para montar o ambiente virtual necessário para desenvolver e executar o projeto.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="justify">
<h2>Coleta de Dados EEG</h2>
<p>
Os dados utilizados neste projeto foram coletados de 17 voluntários que foram submetidos a 6 momentos distintos para coleta dos dados EEG. Os testes aplicados foram os seguintes:
</p>
</div>

<div align="left">
<ul>
  <li>alpha: Estado de relaxamento dos voluntários.</li>
  <li>cafe-1: Voluntário consome um café de má qualidade.</li>
  <li>cafe-2: Voluntário consome um café de boa qualidade.</li>
  <li>chimp: Voluntário realiza um teste cognitivo inspirado no teste "Chimp Test" do Human Benchmark.</li>
  <li>seq: Voluntário realiza um teste cognitivo sequencial inspirado no Human Benchmark.</li>
  <li>react: Voluntário realiza um teste de velocidade de reação inspirado no Human Benchmark.</li>
</ul>
</div>

<div align="justify">
<p>
Esses testes foram realizados usando a plataforma online do Human Benchmark. Você pode encontrar mais informações sobre esses testes e a plataforma em <a href="https://humanbenchmark.com/">Human Benchmark</a>.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="left">
<h2>Estrutura do repositório</h2>
</div>

<div align="justify">
<h3>src</h3>
<p>
Neste diretório, você encontrará os seguintes arquivos e pastas:
</p>
</div>

<div align="left">
  <ul>
    <li><b>data</b>: Pasta que contém scripts necessários para puxar os dados e que também irá armazenar os dados coletados. Esses scripts são responsáveis por obter os sinais EEG brutos de uma fonte externa, o google-cloud, e armazená-los localmente para processamento e análise posterior.</li>
    <li><b>filter</b>: Diretório que contém scripts para processar os dados EEG. Esses scripts são responsáveis por aplicar filtros e técnicas de pré-processamento nos sinais EEG, visando formatar os dados e prepará-los para as etapas posteriores.</li>
    <li><b>setup.sh</b>: (Fazer)</li>
  </ul>
</div>

<div align="justify">
<h3>explorer.ipynb</h3>
<p>
Notebook Jupyter que oferece uma interface para explorar os sinais EEG.
</p>
</div>

<div align="justify">
<h3>environment.yml</h3>
<p>
Arquivo YAML que permite a criação do ambiente virtual necessário para reproduzir o ambiente Anaconda utilizado no projeto.
</p>
</div>

<div align="justify">
<h3>requirements.txt</h3>
<p>
Arquivo que lista os requisitos de software necessários para o projeto, como o google-cloud.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="justify">
<h2>Detalhamento dos dados EEG</h2>
<p>
Os dados EEG utilizados neste projeto estão armazenados na pasta <b>/data</b>. Esses dados são fundamentais para os processos realizados nos scripts Python presentes em <b>src</b> e no notebook <b>explorer.ipynb</b>.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="justify">
<h2>Montando o ambiente virtual</h2>
<p>
Este projeto utiliza a distribuição do <a href="https://www.anaconda.com/products/distribution">Anaconda</a> para criar o ambiente virtual em Python. No entanto, para uma instalação mais enxuta, recomendamos o uso do <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a>.
</p>
</div>

<div align="justify">
<p>
Para reproduzir o ambiente Python necessário para este projeto, acesse o diretório que contém este projeto e execute o seguinte comando no terminal:
</p>
</div>

<pre>
<code>
conda env create -f environment.yml
</code>
</pre>

## Trabalhando com os dados no bucket
