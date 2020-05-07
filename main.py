from Util.header import headers
from Util.query_repos import query_repositorios
from Util.query_issues import query_issues
from Scripts.github_repo_getter import get_repositorios
from Scripts.github_issues_getter import get_issues
import pathlib
import os

def criar_pasta(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("\nDiretório:", path, "não foi criado pois já existe.")

def main_script():
    repositorios = get_repositorios(headers, query_repositorios)
    
    path_repositorios_analisados = str(pathlib.Path().absolute()) + "\\RepositoriosAnalisados"
    criar_pasta(path_repositorios_analisados)
    
    for i, repositorio in enumerate(repositorios):
        top_50_issues = get_issues(headers, query_issues, "DESC" , repositorio)
        bottom_50_issues = get_issues(headers, query_issues, "ASC", repositorio)
        
        # Cria uma pasta dentro de /RepositoriosAnalisados com o nome do repositorio e um indice atras
        # Pega as issues desse repositorio com a query
        # Exporta pra .csv tanto o repositorio quanto a issue
        
main_script()