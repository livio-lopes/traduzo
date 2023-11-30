## O que é projeto Traduzo?
Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, explorando a arquitetura MVC (Model, View e Controller) para criar uma aplicação Server Side. Ou seja, o Back-end (pela controller) fornecerá diretamente a camada View, para a pessoa usuária.

## Quais desafios?
1. Criar a conexão com o MongoDB
2. Criar model para instanciar idiomas, LanguageModel
3. Converter o atributo self.data para Dicionário em LanguageModel
4. Lista todos os Idiomas como Dicionários
5. Renderizar variaveis do backend para o endpoint ` GET "/"`
6. Traduzir o texto através o metodo `POST "/"`
7. Inverter tradução com `POST /reverse`
8. Testar histórico de traduções
9. Criar endpoint para listagem de histórico de traduções
10. Testar exclusão de histórico de traduçõe

## Como iniciar?
1. Clonando o projeto `git clone https://github.com/livio-lopes/traduzo.git`
2. Criando e acesso seu ambiente virtual `python3 -m venv venv && source .venv/bin/activate`
3. Instalando dependencias `python3 -m pip install -r dev-requirements.txt`
4. Subindo o compose, Flask e o Banco `docker compose up translate`
