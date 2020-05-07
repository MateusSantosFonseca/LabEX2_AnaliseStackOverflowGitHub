query_issues = """
{
    repository(name: "{placeholder_nome_repo}", owner: "{placeholder_owner_repo}") {
            name
            nameWithOwner
            primaryLanguage {
                name
            }
        issues(orderBy: {field: COMMENTS, direction: DESC}, first: 50) {
            nodes {
                id
                number
                title
                comments {
                    totalCount
                }
            }
        }
    }
}
"""


