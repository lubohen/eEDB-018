# Data Preparation for Machine Learning

Este projeto oferece uma solução automatizada para a preparação de dados destinados a serem usados em modelos de machine learning. Utilizando a biblioteca `scikit-learn` para tratamento e pré-processamento de dados, facilita a etapa de limpeza e normalização de conjuntos de dados, essencial para a construção de modelos preditivos eficientes.

## Funcionalidades

- Carregamento de dados a partir de arquivos CSV.
- Separação automática de features e variável alvo.
- Codificação de variáveis alvo categóricas.
- Preenchimento de valores ausentes em features numéricas.
- Normalização de features numéricas.
- Divisão de dados em conjuntos de treinamento e teste.
- Salvamento de objetos de pré-processamento para uso futuro.

## Como Começar

### Pré-requisitos

- Python 3.6 ou superior
- scikit-learn
- pandas
- joblib

### Instalação

1. Clone o repositório para sua máquina local:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve incluir:

```
pandas
scikit-learn
joblib
```

### Uso

Para usar este script para preparar seus dados para modelagem, siga os passos abaixo:

1. Certifique-se de que seu conjunto de dados esteja no formato CSV e inclua tanto as features (numéricas e/ou categóricas) quanto a variável alvo.

2. Atualize as variáveis no script, especificando o caminho para seu arquivo de dados, o nome da coluna alvo, e uma lista de features numéricas.

3. Execute o script para processar seus dados:

```
python data_preparation.py
```

4. Os conjuntos de dados de treinamento e teste processados serão salvos no diretório especificado, juntamente com os objetos de pré-processamento.

## Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para forkar o projeto, fazer suas alterações e criar um pull request para que suas melhorias sejam incorporadas ao projeto.

## Licença

Este projeto é distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais informações.

## Contato

Seu Nome - [@seuTwitter](https://twitter.com/seuTwitter) - email@example.com

Link do Projeto: [https://github.com/seu-usuario/seu-repositorio](https://github.com/seu-usuario/seu-repositorio)