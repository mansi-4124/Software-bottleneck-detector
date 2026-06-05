from app.services.github_service import GitHubService


def test_parse_repository_data():
    sample_response = {
        "id": 123,
        "name": "test-repo",
        "full_name": "john/test-repo",
        "owner": {
            "login": "john"
        },
        "description":"This was a test repo",
        "default_branch": "main",
        "language": "Python",
        "stargazers_count": 50
    }

    result = GitHubService.parse_repository(
        sample_response
    )

    assert result["github_id"] == 123
    assert result["name"] == "test-repo"
    assert result["owner"] == "john"