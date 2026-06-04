"""
Tests for GitHub service.
"""

from unittest.mock import patch

from app.services.github_service import GitHubService


@patch("app.services.github_service.requests.get")
def test_fetch_repository_details(mock_get):
    """
    Verify repository information
    is correctly extracted from
    GitHub API response.
    """

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "id": 123,
        "name": "test-repo",
        "owner": {
            "login": "openai"
        },
        "html_url": "https://github.com/openai/test-repo"
    }

    service = GitHubService()

    repo = service.get_repository(
        owner="openai",
        repo="test-repo"
    )

    assert repo["id"] == 123
    assert repo["name"] == "test-repo"
    assert repo["owner"] == "openai"