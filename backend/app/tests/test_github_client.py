from unittest.mock import patch

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
    headers = GitHubClient.build_headers(
        "token123"
    )

    assert headers["Authorization"] == "Bearer token123"


@patch("app.services.github_client.requests.get")
def test_fetch_repository(mock_get):

    mock_response = mock_get.return_value

    mock_response.json.return_value = {
        "id": 1,
        "name": "react"
    }

    mock_response.raise_for_status.return_value = None

    client = GitHubClient(token="fake-token")

    result = client.fetch_repository(
        owner="facebook",
        repo="react"
    )

    assert result["name"] == "react"