from dotenv import load_dotenv
import os
import google.generativeai as genai

# carrega variáveis de ambiente de .env
load_dotenv()

# configura a API Key
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# modelo usado Gemini Pro
model = genai.GenerativeModel('gemini-2.0-flash')

def gerar_plano_de_estudos(materias, tempo_disponivel, prioridade=None, observacao=''):
    prompt_base = f'''
    Crie um plano de estudos personalizado considerando as seguintes informações:
    
    Matérias/Cursos: {materias}
    Tempo Total Disponível na Semana: {tempo_disponivel}
    '''

    if prioridade:
        prompt_base += f'\nPrioridade: {prioridade}'
    else:
        prompt_base += '\nPrioridade: Não especificada.'

    prompt_base += f'\nObservações Adicionais: {observacao if observacao else 'Nenhuma'}'

    prompt = prompt_base + '''

    O plano de estudos deve ser útil e incluir:
    - Uma sugestão de distribuição do tempo de estudo ao longo da semana (semanal ou diária).
    - Sugestões de métodos de estudo eficazes e criativos para cada matéria.
    - **Para cada matéria, inclua dicas de recursos relevantes para estudo, como sites, cursos online, blogs, canais do YouTube ou outras fontes de informação de qualidade.**
    - Dicas de como manter a motivação e evitar a procrastinação.
    - Adapte o plano de estudos com base na prioridade especificada (se fornecida).

    Formate o plano de estudos de forma clara e organizada, com seções para cada dia ou bloco de tempo, as matérias a serem estudadas e as sugestões de métodos e recursos.
    '''

    # envia prompt para Gemini e pega a resposta
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    materias = input("Digite as matérias/cursos a estudar (separadas por vírgula): ")
    tempo_disponivel = input("Digite o tempo total disponível para estudar na semana (em horas): ")
    prioridade = input("Qual a prioridade dos seus estudos? (opcional, deixe em branco se não houver): ")
    observacao = input("Alguma observação adicional para o plano de estudos? (opcional): ")

    prompt_gerado = gerar_plano_de_estudos(materias, tempo_disponivel, prioridade, observacao)
    print("\nPrompt Gerado:\n")
    print(prompt_gerado)

