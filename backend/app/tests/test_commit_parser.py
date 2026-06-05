from app.services.github_service import (
    GitHubService
)


def test_parse_commit():
    data = {
        "sha": "abc123",
        "commit": {
            "message": "initial",
            "author": {
                "name": "Mansi",
                "email": "test@test.com",
                "date": "2026-06-05T10:00:00Z"
            }
        }
    }

    parsed = (
        GitHubService.parse_commit(data)
    )

    assert parsed["github_sha"] == "abc123"
    assert parsed["message"] == "initial"