# 📦 Sistema de Marcação de Produtos (Terminal)

Este projeto é um sistema simples de marcação de produtos desenvolvido para rodar no terminal. Ele permite o gerenciamento completo de uma lista de produtos, com funcionalidades de **adicionar**, **editar**, **excluir**, **visualizar** e **exportar** os dados.

## ✨ Funcionalidades

- ➕ Adicionar novos produtos com nome e preço  
- ✏️ Alterar o preço de produtos já cadastrados  
- 🗑️ Remover produtos da lista  
- 📋 Visualizar os produtos em uma tabela formatada diretamente no terminal  
- 📄 Exportar a tabela para um arquivo `.txt`  
- 📊 Exportar a tabela para um arquivo `.xlsx` (Excel)

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) – manipulação de dados e exportação para Excel
- [Tabulate (opcional)](https://pypi.org/project/tabulate/) – para exibição mais bonita da tabela no terminal (se usado)

## 🚀 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/ExtremeCodeX/Sistema_Mercado

## Instruções para rodar o projeto

1. Clone o repositório:

   ```bash
   git clone <URL do repositório>
   ```

2. Entre na pasta do projeto:

   ```bash
   cd Sistema_Mercado
   ```

3. Crie a pasta `data/` (caso não tenha sido criada):

   ```bash
   mkdir data
   ```

4. O arquivo `produtos.json` será automaticamente gerado dentro da pasta `data/` quando você adicionar produtos.

5. Para rodar o sistema:

   ```bash
   python main.py
   ```

## 📁 Estrutura do repositório

```
Sistema_Mercado/
├── main.py
├── LICENSE
├── README.md
├── data/
│   └── produtos.json
```

## 📝 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

