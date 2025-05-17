# Assistente de Plano de Estudos Personalizado com Gemini AI

Este projeto foi feito como desafio da Imersão IA da Alura, é um assistente inteligente que usa a tecnologia Gemini AI do Google para criar planos de estudos sob medida para você. Basta dizer o que você precisa estudar, quanto tempo tem disponível e, opcionalmente, suas prioridades e dificuldades. A IA cuidará do resto, sugerindo um cronograma com métodos de estudo e links úteis.

## Funcionalidades

* **Criação Personalizada de Plano de Estudos:** Com base nas suas matérias, tempo disponível e prioridades, a IA gera um plano de estudos único para atender às suas necessidades.
* **Sugestão de Distribuição de Tempo:** O assistente propõe como você pode dividir seu tempo de estudo ao longo da semana ou dos dias, ajudando a organizar sua rotina.
* **Métodos de Estudo Eficazes e Criativos:** Além do cronograma, a IA sugere diferentes maneiras de estudar que podem tornar o aprendizado mais dinâmico e eficiente para cada matéria.
* **Indicação de Recursos de Aprendizagem:** Para cada disciplina, o plano de estudos inclui links e dicas de onde encontrar materiais de estudo de qualidade, como sites educativos, cursos online, blogs e canais de vídeo.
* **Dicas para Manter a Motivação:** O assistente oferece conselhos práticos para ajudar você a se manter motivado e a evitar a procrastinação durante seus estudos.
* **Adaptação Inteligente:** O plano de estudos leva em consideração suas prioridades e observações, como dificuldades em certas matérias, para oferecer um cronograma mais eficaz.
* **Formato Fácil de Seguir:** O plano de estudos é apresentado de forma clara e organizada, usando uma linguagem simples e marcadores visuais para facilitar a leitura e o acompanhamento.

## Como Usar

1.  **Primeiros Passos:**
    * Certifique-se de ter o Python instalado no seu computador.
    * Você precisará de uma chave especial (API Key) do Google para que o programa funcione. Você pode obter essa chave seguindo as instruções no [Google AI Studio](https://makersuite.google.com/app/apikey).
    * Depois de obter a chave, salve-a em um arquivo chamado `.env` na mesma pasta do programa, da seguinte forma: `GOOGLE_API_KEY=SUA_API_KEY_AQUI` (substitua `SUA_API_KEY_AQUI` pela sua chave real).

2.  **Rodando o Programa:**
    * Abra o terminal (ou prompt de comando) na pasta onde você salvou os arquivos do projeto.
    * Execute o seguinte comando:
        ```bash
        python assistente_estudos.py
        ```
    * O programa fará algumas perguntas sobre o que você precisa estudar e quanto tempo você tem disponível. Responda às perguntas no terminal.
    * Após fornecer as informações, o seu plano de estudos personalizado será gerado e exibido na tela.

## Dependências

* `google-generativeai`: A biblioteca que permite a comunicação com a inteligência artificial do Google.
* `python-dotenv`: Uma ferramenta para ajudar a usar a sua chave de API de forma segura.

## Notas

* Mantenha o arquivo `.env` com a sua chave de API em segurança e não o compartilhe.
* O plano de estudos gerado é uma sugestão e você pode adaptá-lo da maneira que achar melhor.
