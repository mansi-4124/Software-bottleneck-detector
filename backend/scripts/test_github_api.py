from app.services.github_client import GitHubClient

client = GitHubClient()

repo = client.fetch_repository(
    owner="facebook",
    repo="react"
)

print(repo["name"])
print(repo["stargazers_count"])