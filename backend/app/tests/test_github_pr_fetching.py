from app.services.github_client import (
    GitHubClient
)


def test_pull_request_url():
    client = GitHubClient()

    data = client.fetch_pull_requests(
        owner="facebook",
        repo="react",
    )

    assert isinstance(
        data,
        list
    )