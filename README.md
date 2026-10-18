# Geo-Explorer

O Geo-Explorer é um projeto de portfólio inspirado no desafio da DIO. Ele simula uma plataforma de aprendizagem com três comandos: consulta de trilhas, geração de desafios e emissão de certificados fictícios.

## Requisitos

- Python 3.10 ou superior
- `pytest` para executar os testes

## Executar

No diretório do projeto:

```bash
python -m geo_explorer.cli trilha Python iniciante
python -m geo_explorer.cli desafio JavaScript intermediário
python -m geo_explorer.cli certificado "Seu Nome" Python iniciante
```

Mensagens de erro são exibidas quando a trilha não existe ou quando o nome do certificado está vazio.

## Testes

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Servidor MCP

O arquivo `geo_explorer/mcp_server.py` implementa um servidor MCP mínimo usando JSON-RPC por entrada e saída padrão. Ele expõe as ferramentas `trilha`, `desafio` e `certificado`.

Para iniciar:

```bash
python -m geo_explorer.mcp_server
```

O servidor foi mantido sem dependência externa para deixar o fluxo didático e fácil de inspecionar. Um cliente MCP pode enviar mensagens JSON-RPC, como `initialize`, `tools/list` e `tools/call`.

## Organização

- `data/tracks.json`: base fictícia de trilhas;
- `geo_explorer/core.py`: regras de negócio;
- `geo_explorer/cli.py`: interface de linha de comando;
- `geo_explorer/mcp_server.py`: integração MCP por JSON-RPC;
- `tests/`: testes automatizados.

## Melhorias realizadas

- Busca de tecnologia e nível sem diferenciação entre maiúsculas e minúsculas;
- mensagens de erro amigáveis;
- validação de nome no certificado;
- testes para caminho feliz e falhas importantes;
- servidor MCP com schema das ferramentas;
- separação entre dados, regras de negócio e interfaces.

## O que aprendi

O projeto pratica organização modular, leitura de dados JSON, criação de uma CLI, validação de entradas, testes automatizados e a ideia de um servidor MCP como uma camada que disponibiliza funcionalidades para outras ferramentas.

## Segurança

O projeto não usa credenciais, tokens ou serviços externos. Antes de publicar no GitHub, revise arquivos adicionados localmente e não inclua segredos.
