# Assistente de Plano de Estudos Personalizado com Gemini AI

Este projeto é um assistente de plano de estudos personalizado que utiliza a API do Google Gemini para gerar um cronograma de estudos criativo e útil, com sugestões de métodos de estudo e recursos online relevantes para as matérias fornecidas pelo usuário.

## Funcionalidades

* **Entrada Personalizada:** O usuário pode inserir as matérias/cursos a estudar, o tempo total disponível para estudo na semana, a prioridade (opcional) e observações adicionais para direcionar a geração do plano.
* **Plano de Estudos Criativo:** O Gemini AI gera um plano de estudos que inclui uma sugestão de distribuição do tempo, métodos de estudo eficazes e criativos.
* **Sugestões de Recursos:** Para cada matéria, o plano inclui dicas de recursos de estudo como sites, cursos online, blogs e canais do YouTube.
* **Dicas de Motivação:** O plano também oferece dicas para manter a motivação e evitar a procrastinação.
* **Formato Organizado:** O plano de estudos é formatado de forma clara e organizada, utilizando Markdown.

## Como Usar

1.  **Pré-requisitos:**
    * Python 3 instalado no seu sistema.
    * `pip` (gerenciador de pacotes do Python) instalado.
    * Uma API Key válida do Google Gemini (obtida através do Google AI Studio).
    * Uma conta no GitHub (para hospedar o projeto).

2.  **Configuração:**
    * Clone este repositório para o seu computador:
        ```bash
        git clone [https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content)
        cd [nome do seu repositório]
        ```
    * Crie um arquivo `.env` na raiz do projeto e adicione sua API Key do Google Gemini:
        ```
        GOOGLE_API_KEY=SUA_API_KEY_AQUI
        ```
        **Substitua `SUA_API_KEY_AQUI` pela sua chave real.**
    * Crie um ambiente virtual (recomendado):
        ```bash
        python -m venv venv
        source venv/bin/activate  # No macOS/Linux
        venv\Scripts\activate  # No Windows (cmd)
        .\venv\Scripts\Activate.ps1  # No Windows (PowerShell)
        ```
    * Instale as dependências:
        ```bash
        pip install -r requirements.txt
        ```
        (Se você ainda não tem o `requirements.txt`, pode criá-lo com `pip freeze > requirements.txt` após instalar as bibliotecas `google-generativeai` e `python-dotenv`).

3.  **Execução:**
    * Certifique-se de que o ambiente virtual esteja ativado.
    * Execute o script principal (`assistente_estudos.py` ou o nome que você deu ao arquivo):
        ```bash
        python assistente_estudos.py
        ```
    * O script irá solicitar que você insira as informações sobre as matérias, tempo disponível, prioridade (opcional) e observações (opcional).
    * Após inserir as informações, o plano de estudos gerado pelo Gemini AI será exibido no terminal.

## Dependências

* `google-generativeai`: Biblioteca do Google para interagir com os modelos Gemini.
* `python-dotenv`: Para carregar variáveis de ambiente de um arquivo `.env`.

Você pode instalar todas as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt