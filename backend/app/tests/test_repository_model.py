from app.models.repository import Repository


def test_repository_model_creation():

    repo = Repository(
        github_id=123456,
        name="software-bottleneck-detector",
        full_name="mansi/software-bottleneck-detector",
        owner="mansi",
        default_branch="main",
        language="Python",
        stars=10
    )

    assert repo.github_id == 123456
    assert repo.name == "software-bottleneck-detector"
    assert repo.owner == "mansi"

