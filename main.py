from Util.header import headers
from Util.query_repos import query_repositorios
from Util.query_issues import query_issues
from Scripts.github_repo_getter import get_repositorios
from Scripts.github_issues_getter import get_issues
from Scripts.exportador_csv import exportar_arquivos_csv
import pathlib
import os
import shutil

def criar_pasta(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"\nDiretório: {path} não foi criado pois já existe.")
        
def deletar_pasta(path):
    try:
        shutil.rmtree(path)
    except:
        print(f"\nDiretório: {path} não pode ser excluido. Favor apagá-lo manualmente.")

def main_script():
    repositorios = get_repositorios(headers, query_repositorios)
    
    path_repositorios_analisados = str(pathlib.Path().absolute()) + "\\RepositoriosAnalisados"
    
    deletar_pasta(path_repositorios_analisados)
    criar_pasta(path_repositorios_analisados)
    
    for i, repositorio in enumerate(repositorios):
        top_issues = get_issues(headers, query_issues, "DESC" , repositorio, path_repositorios_analisados)
        bottom_issues = get_issues(headers, query_issues, "ASC", repositorio, path_repositorios_analisados)
            
        path_repo_analisado = path_repositorios_analisados + "\\" + "{:04n}".format(i) + "_" + repositorio['name']
        criar_pasta(path_repo_analisado)
            
        exportar_arquivos_csv(path_repo_analisado, repositorio, top_issues, bottom_issues)
            
        print(f"\nO repositório {repositorio['name']} foi analisado e os resultados retornados foram exportados para um arquivo .csv com sucesso.") 
            
    print("\nO Script foi finalizado com sucesso.")   

main_script()