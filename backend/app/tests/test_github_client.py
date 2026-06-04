from app.services.github_client import GitHubClient


def test_repo_url_generation():
    url = GitHubClient.build_repo_url(
        owner="facebook",
        repo="react"
    )

    assert (
        url ==
        "https://api.github.com/repos/facebook/react"
    )

def test_headers_present():
    headers = GitHubClient.build_headers("token123")

    assert headers["Authorization"] == "Bearer token123"

def test_fetch_public_repo():
    client = GitHubClient()

    data = client.fetch_repository(
        owner="facebook",
        repo="react"
    )

    assert data["name"] == "react"