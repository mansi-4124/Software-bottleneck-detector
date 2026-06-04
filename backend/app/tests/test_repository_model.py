from app.models.repository import Repository


def test_repository_model_creation():

    repo = Repository(
        github_repo_id=123,
        name="backend",
        owner="openai"
    )

    assert repo.github_repo_id == 123
    assert repo.name == "backend"
    assert repo.owner == "openai"