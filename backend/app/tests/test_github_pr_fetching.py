from unittest.mock import Mock
from unittest.mock import patch

from app.services.github_client import (
    GitHubClient
)


@patch(
    "app.services.github_client.requests.get"
)
def test_pull_request_url(
    mock_get
):
    mock_response = Mock()

    mock_response.json.return_value = [
        {
            "number": 123,
            "title": "Test PR"
        }
    ]

    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    client = GitHubClient(
        token="fake-token"
    )

    data = client.fetch_pull_requests(
        owner="facebook",
        repo="react",
    )

    assert isinstance(
        data,
        list
    )

    assert data[0]["number"] == 123