<h1>README - Projeto EEG_coffee_alert</h1>

<div align="justify">
<h2>Introdução ao projeto</h2>
<p>
Bem-vindo ao projeto EEG_coffee_alert! Este é um repositório dedicado a um projeto de análise de dados EEG utilizando Inteligência Artificial. Aqui você encontrará informações sobre a coleta de dados, a estrutura do repositório, detalhes sobre a base de dados utilizada e instruções para montar o ambiente virtual necessário para desenvolver e executar o projeto.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="justify">
<h2>Coleta de Dados EEG</h2>
<p>
Os dados utilizados neste projeto foram coletados de 17 voluntários que foram submetidos a 6 momentos distintos de amostragem. Os testes aplicados foram os seguintes:
</p>
</div>

<div align="left">
<ul>
  <li>alpha: Somente um estado de relaxamento dos voluntários.</li>
  <li>cafe-1: Os voluntários consumiram um café de má qualidade.</li>
  <li>cafe-2: Os voluntários consumiram um café de boa qualidade.</li>
  <li>chimp: Os voluntários realizaram um teste cognitivo chamado "Chimp Test" do Human Benchmark.</li>
  <li>seq: Os voluntários realizaram um teste cognitivo chamado "Sequence Memory" do Human Benchmark.</li>
  <li>react: Os voluntário realizam um teste de velocidade de reação chamado "Reaction Time" no Human Benchmark.</li>
</ul>
</div>

<div align="justify">
<p>
Plataforma utilizada: <a href="https://humanbenchmark.com/">Human Benchmark</a>
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

<div align="justify">
  <ul>
    <li><b>data</b>: Pasta que contém scripts necessários para puxar os dados e que também irá armazenar os dados coletados. Esses scripts são responsáveis por obter os sinais EEG de uma fonte externa, o google-cloud, e armazená-los localmente para processamento e análise posterior.</li>
    <li><b>filter</b>: Diretório que contém scripts para processar os dados EEG. Esses scripts são responsáveis por aplicar filtros e técnicas de pré-processamento nos sinais EEG, visando formatar os dados e prepará-los para as etapas posteriores envolvendo IA.</li>
    <li><b>setup.sh</b>: (Fazer)</li>
  </ul>
</div>

<div align="justify">
<h3>explorer.ipynb</h3>
<p>
O notebook "EEG Explorer" é uma ferramenta de análise de dados de eletroencefalografia (EEG) que permite visualizar e plotar sinais de diferentes canais cerebrais. Ele utiliza bibliotecas como pandas, numpy, scipy, matplotlib e plotly para processar e exibir os dados. O usuário pode importar arquivos CSV contendo informações do EEG e selecionar os canais que deseja visualizar. A ferramenta também possui interatividade, permitindo ajustar o tamanho da janela móvel e selecionar diferentes arquivos e canais para análise. Isso possibilita uma análise mais detalhada dos sinais EEG, com gráficos de média móvel e primeira derivada para uma melhor compreensão dos dados.
</p>
</div>

<div align="justify">
<h3>environment.yml</h3>
<p>
Arquivo yaml que permite a criação do ambiente Anaconda necessário para reproduzir o projeto. Mais adiante, na seção <b>Montando o ambiente virtual</b> será explicado como utilizar esse arquivo.
</p>
</div>

<div align="justify">
<h3>requirements.txt</h3>
<p>
Arquivo que lista os requisitos de software necessários para o projeto, como o google-cloud. Tenha certeza de possuir cada um deles.
</p>
</div>

<!------------------------------------------------------------------------------------------------------------------------------>

<div align="justify">
<h2>Detalhamento dos dados EEG</h2>
<p>
Os dados EEG utilizados neste projeto estão armazenados na pasta <b>/data</b>. Esses dados são fundamentais para os processos realizados nos scripts Python presentes em <b>src</b> e no notebook <b>explorer.ipynb</b>.
</p>
</div>

<div align="justify">
<p>
Os dados estão separados em diversos arquivos, cada um representando um momento específico de um voluntário. O formato do nome do arquivo segue o padrão:
    <code>&lt;nome do teste&gt;_&lt;ID do voluntário&gt;</code> (por exemplo: voluntário 1 durante o teste alpha: <code>alpha_1</code>).
</p>
<p>
Cada arquivo CSV possui as seguintes colunas:
</p>
  <ul>
    <li><code>Index</code>: Índice do dado no arquivo.</li>
    <li><code>Fp1</code>: Sinal EEG próximo do lobo frontal do cérebro.</li>
    <li><code>Fp2</code>: Sinal EEG próximo do lobo frontal do cérebro.</li>
    <li><code>C3</code>: Sinal EEG próximo do lobo pariental do cérebro.</li>
    <li><code>C4</code>: Sinal EEG próximo do lobo pariental do cérebro.</li>
    <li><code>P7</code>: Sinal EEG próximo do lobo temporal do cérebro.</li>
    <li><code>P8</code>: Sinal EEG próximo do lobo temporal do cérebro.</li>
    <li><code>O1</code>: Sinal EEG próximo do lobo occiptal do cérebro.</li>
    <li><code>O2</code>: Sinal EEG próximo do lobo occiptal do cérebro.</li>
    <li><code>Timestamp</code>: Registro do tempo da coleta em segundos.</li>
  </ul>
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

<div align="center">
<pre>
<code>
conda env create -f environment.yml
</code>
</pre>
</div>

## Trabalhando com os dados no bucket
