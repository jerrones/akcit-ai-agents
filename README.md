# Agentes de IA: LangChain + Gemini (AKCIT-UFG)

Este repositório contém a implementação prática de agentes inteligentes utilizando o framework **LangChain** e o modelo **Google Gemini**. O projeto faz parte do curso de **Agentes de Inteligência Artificial** do Centro de Competência Embrapii em Tecnologias Imersivas (AKCIT – Universidade Federal de Goiás).

## Tecnologias e Ferramentas

- **Python 3.12**
- **LangChain:** Framework para orquestração de LLMs.
- **Google Gemini API:** Modelo de linguagem de larga escala.
- **Python-dotenv:** Gerenciamento de variáveis de ambiente.

## Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone git@github.com:jerrones/akcit-ai-agents.git
cd akcit-ai-agents
```

### 2. Configurar Ambiente Virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install langchain langchain-google-genai python-dotenv
```

### 4. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:

```bash
GOOGLE_API_KEY=sua_chave_aqui
```

### 5. Rodar a aplicação

```bash
python3 main.py
```
