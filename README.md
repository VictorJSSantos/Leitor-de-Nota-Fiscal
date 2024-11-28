<div align="justify">

## Descrição do projeto

Esse arquivo foi criado em 2020, quando eu estava nos primeiros passos, com o objetivo de fazer leitura de dados de notas fiscais de forma simplifiada para poder confrontar valores entre (1) valores presentes em nota (peso, valor da carga, etc..) com os (2) valores cobrados por parceiros de transportes, os quais baseavam suas regras de pricing nestas informações. O problema enfrentado à época era o aumento de volume de notas, conhecimentos de transportes (CTe's) e outros arquivos fiscais que recebíamos e o alto valor financeiro dos pagamentos, que era relevante para a empresa, sendo um dos mais relevantes centros de custo da empresa.
Esse fluxo era aplicado para as notas fiscais recebidas, já para as emitidas nós acessávamos através de consultas SQL o BigQuery da GCP para coletar as informações contidas em nossas notas e finalizar este processo.

## Objetivo

O arquivo deveria ser "escanear" uma pasta e a partir desta pasta, gerar uma lista de arquivos xml a serem lidos e processar a leitura dos dados em cada um dos arquivos. Por fim, deveria montar as informações num dataframe e servir um arquivo em formato pronto para realização de análises posteriores.

## Setup do Ambiente

1. Realize o clone do repositório:
  > https://github.com/VictorJSSantos/Leitor-de-Nota-Fiscal.git

2. Recomendado:: Crie o ambiente virtual: 
  > python -m venv venv

3. Ativando o ambiente virtual: 
No Windows:
  > venv\Scripts\activate
No Linux:
  > source venv/bin/activate

4. Configure o interpretador python no ambiente virtual:
Ctrl + Shift + P para abrir a paleta de comandos.
  > Digite Python: Select Interpreter e escolha o Python dentro da pasta venv.

5. Atualize o pip para garantir a instalação devida das dependências:
  > python -m pip install --upgrade pip

5. Instale as dependências:
  > pip install -r requirements.txt



</div>
