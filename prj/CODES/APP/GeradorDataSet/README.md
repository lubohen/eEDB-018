# Spotify Track Features Extractor

Este projeto fornece uma ferramenta Python para buscar características de áudio de faixas específicas através da API do Spotify e armazenar essas informações em um arquivo CSV. Ele é projetado para ser fácil de usar e extensível, permitindo que usuários coletem dados de música para análise, recomendação de músicas, análise de tendências musicais, ou estudos acadêmicos relacionados à música. Nesse caso focado em complementar uma base de dados pré-existente com as marcações dos quandrantes conforme o Modelo Circumplexo de Russel.

## Funcionalidades

- Autenticação automática no Spotify usando credenciais de cliente (ID do cliente e segredo do cliente).
- Busca por características de áudio de faixas específicas, como acústica, dançabilidade, energia, entre outras.
- Carregamento de um conjunto de faixas a partir de um arquivo CSV.
- Salvamento das características de áudio e informações adicionais em um arquivo CSV.
- Log de faixas não encontradas na API do Spotify.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.6+
- Bibliotecas Python: `requests`, `pandas`
- Credenciais do Spotify (ID do cliente e Segredo do cliente)

### Instalação

1. Clone este repositório ou baixe os arquivos do projeto.
2. Instale as dependências necessárias executando `pip install -r requirements.txt` no diretório do projeto.
3. Configure suas variáveis de ambiente para incluir `SPOT_CLIENT_ID` e `SPOT_CLIENT_SECRET` com suas credenciais do Spotify.

### Uso

1. Prepare um arquivo CSV com as faixas que deseja analisar. O arquivo deve ter as colunas `Title`, `Artist`, `GenresStr`, e `Quadrant`.
2. Atualize a variável `DATA_FILE_PATH` no script para apontar para o seu arquivo CSV.
3. Execute o script com `python spotify_track_features_extractor.py`.

## Contribuindo

Contribuições são bem-vindas! Se você tem uma sugestão para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório e enviar um pull request. Você também pode abrir uma issue com a tag "melhoria".

## Licença

Este projeto é distribuído sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

Se você tiver alguma dúvida ou quiser entrar em contato, por favor, abra uma issue no repositório do GitHub.