import requests

def requisitar_issues(headers, query):
    request = requests.post('https://api.github.com/graphql', json = {'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 502:
        return requisitar_issues(query, headers)
    else:
        raise Exception("A query falhou: {}. {}".format(request.status_code, query))

def get_issues(headers, query_issues, orientacao_ordenacao, repositorio):
    nome_owner_repositorio = repositorio['nameWithOwner'].split('/')
    owner_repositorio = nome_owner_repositorio[0]
    nome_repositorio = nome_owner_repositorio[1]

    query_issues_final = query_issues.replace("{placeholder_nome_repo}", nome_repositorio)
    query_issues_final = query_issues_final.replace("{placeholder_owner_repo}", owner_repositorio)
    query_issues_final = query_issues_final.replace("{placeholder_orientacao_issue}", orientacao_ordenacao)
    
    response = requisitar_issues(headers, query_issues_final)
    issues_retornadas = response["data"]["repository"]["issues"]["nodes"]

    print(f"\nA recuperação das issues do repositório {nome_repositorio} foi finalizada.") 
    return issues_retornadas