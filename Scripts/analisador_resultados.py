import re

class LinguagensAnalisadas():
    linguagens_analisadas = []
    
def string_strip_nao_alphanumericos(string):
    regex_pattern = re.compile(r'\W+')
    return re.sub(regex_pattern, '', string)    

def get_numero_mencoes_issues(issues, questions, repositorio):
    mencoes = 0
    for issue in issues:
        titulo_splitado = issue['title'].split(" ")
        titulo_splitado = [string_strip_nao_alphanumericos(fragmento.lower().strip()) for fragmento in titulo_splitado]
        titulo_splitado_filtrado = list(filter(None, titulo_splitado))
        for question in questions['items']:
            question_tags = question['tags'].split(',')
            question_tags = [tag.lower().strip() for tag in question_tags]
            if (set(titulo_splitado_filtrado).intersection(question_tags)):
                mencoes += 1
                
    return str(mencoes)

def get_mencoes_linguagens(questions, repositorio, linguagem_repositorio):
    linguagem_repositorio = linguagem_repositorio.lower()
    mencoes_linguagem = 0
    mencoes_linguagem_sem_repetir = 0
    
    for question in questions['items']:
        question_tags = question['tags'].split(',')
        question_tags = [tag.lower().strip() for tag in question_tags]
        if (linguagem_repositorio in question_tags):
            mencoes_linguagem += 1
            if(linguagem_repositorio not in LinguagensAnalisadas.linguagens_analisadas):
                mencoes_linguagem_sem_repetir += 1
    
    if(linguagem_repositorio != "Vazio" and linguagem_repositorio not in LinguagensAnalisadas.linguagens_analisadas):
        LinguagensAnalisadas.linguagens_analisadas.append(linguagem_repositorio)
        
    return f"{mencoes_linguagem},{mencoes_linguagem_sem_repetir}"

def analisar_resultados(questions, repositorio, top_issues, bottom_issues):
    linguagem_repositorio = ""
    
    if(repositorio.get('primaryLanguage') is None):
        linguagem_repositorio = "Vazio"
    else:
        linguagem_repositorio = repositorio['primaryLanguage']['name']
    
    mencoes_linguagens = get_mencoes_linguagens(questions, repositorio, linguagem_repositorio)
    mencoes_top_issues = get_numero_mencoes_issues(top_issues, questions, repositorio)
    mencoes_bottom_issues = get_numero_mencoes_issues(bottom_issues, questions, repositorio)
    
    resultado = f"{repositorio['name']},{linguagem_repositorio},{mencoes_linguagens},{mencoes_top_issues},{mencoes_bottom_issues}"
    return resultado